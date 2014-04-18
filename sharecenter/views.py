from django.shortcuts import render, redirect,get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from sharecenter.forms import ToolCreateForm
from sharecenter.models import Tool, Shed
from notifications.models import Notification
import notifications.NoticeType as NoticeType

@login_required
def create_tool(request, template_name='tools/create_tool.html'):
    """
    Create a new tool with data from request and add it to database.
    """
    if request.method == 'POST':
        form = ToolCreateForm(data=request.POST)
        if form.is_valid():
            shed = request.user.shed_owned.all()[0]
            tool = Tool(
                name=form.cleaned_data['name'],
                category=form.cleaned_data['category'],
                description=form.cleaned_data['description'],
                owner=request.user,
                shed=shed
            )
            tool.save()
            Notification.objects.create(recipient=request.user, 
                                                    sender=request.user,
                                                    tool=tool,
                                                    shed=shed,
                                                    notice_type=NoticeType.ALERT,
                                                    action="created")                                        
            url = reverse('tool_detail', kwargs={'tool_id':tool.id})
            return HttpResponseRedirect(url)
    else: 
        form = ToolCreateForm()

    return render(request, template_name, {'form': form})

@login_required
def delete_tool(request, tool_id):
    tool = get_object_or_404(Tool, pk=tool_id)
    if request.user == tool.owner and tool.is_available():
        tool.delete()
    return redirect('my_tools')


@login_required
def my_tools(request, template_name='tools/my_tools.html'):
    """
    Display a table containing the user's tools. 
    """
    tool_list = request.user.tool_owned.all()
    borrow_list = Tool.objects.filter(borrower=request.user.id)
    return render(request, template_name, {'tool_list':tool_list, 'borrow_list':borrow_list})

@login_required
def edit_tool(request, tool_id, template_name='tools/edit_tool.html'):
    """
    Update tool info with data from request
    """
    tool = get_object_or_404(Tool, pk=tool_id)
    if request.user == tool.owner:
        if request.method == 'POST':
            form = ToolCreateForm(data=request.POST, instance=tool)
            if form.is_valid:  
                form.save()
                url = reverse('tool_detail', kwargs={'tool_id':tool.id})
                return HttpResponseRedirect(url)
        else:
            form = ToolCreateForm(instance=tool)
        return render(request, template_name, {'form':form, 'tool':tool}) #no editing done
    else:
        url = reverse('tool_detail', kwargs={'tool_id':tool.id})
        return HttpResponseRedirect(url)

@login_required
def borrow_tool(request, tool_id):
    """
    Set selected tool as borrowed
    """
    tool = get_object_or_404(Tool, pk=tool_id)
    if tool.is_available():
        tool.borrow_tool(request.user)
        tool.save()
    # send borrow request

    url = reverse('tool_detail', kwargs={'tool_id':tool.id})
    return HttpResponseRedirect(url)

@login_required
def return_tool(request, tool_id):
    """
    Set selected tool as returned
    """
    tool = get_object_or_404(Tool, pk=tool_id)
    if tool.borrower == request.user:
        tool.return_tool()
        tool.save()
    url = reverse('tool_detail', kwargs={'tool_id':tool.id})
    return HttpResponseRedirect(url)

@login_required
def tool_detail(request,  tool_id, template_name='tools/tool_detail.html'):
    """
    Display tool info
    """
    tool = get_object_or_404(Tool, pk=tool_id)
    return render(request, template_name, {'tool':tool})

@login_required
def my_sheds(request, template_name='sheds/my_sheds.html'):
    """
    Display table containing user's sheds. 
    """
    shed_list = request.user.shed_owned.all()
    return render(request, template_name, {'shed_list':shed_list})

@login_required
def shed_detail(request, shed_id, template_name='sheds/shed_detail.html'):
    """
    Display shed info, tool list as table
    """
    shed = get_object_or_404(Shed, pk=shed_id)
    tool_list = shed.shed_tools.all()
    return render(request, template_name, {'shed':shed, 'tool_list':tool_list})

#def create_shed(request, template_name='sheds/create_shed.html'):

  #  if request.method == 'POST':
    #    shed = ShedCreateForm(data=request.POST);
      #  shed.owner = request.user.id;
       # shed.toolLimit = request.toolLimit;
       # shed.save();
        #return redirect('user_home')#go to home page
    #else:
     #   form = ShedCreateForm()
        
    #return render(request, template_name, {'form': form})# no shed created

@login_required
def share_zone(request, template_name='sheds/share_zone.html'):
    """
    Display table with all sheds in share zone
    """
    shed_list = Shed.objects.filter(postal_code=request.user.profile.postal_code)
    return render(request, template_name, {'shed_list':shed_list})






# ============ Borrow Request Views ============
import sharecenter.RequestStatus as RequestStatus

@login_required
def approve_borrow_request(request, br_id):
    """
    Approve borrow request
    """
    borrow_request  = get_object_or_404(BorrowRequest, pk=br_id)
    # check if user is recipient of the borrow request
    if borrow_request.recipient == request.user:
        tool = get_object_or_404(Tool, pk=borrow_request.tool.id);
        # check if owner of tool is the recipient of the borrow request
        if tool.owner == request.user and tool.is_available():
            tool.borrow_tool(borrow_request.sender);
            tool.save();
            # notify requester that the request was approved
            Notification.objects.create(recipient=borrow_request.sender, 
                                                        sender=request.user,
                                                        tool=tool,
                                                        notice_type=NoticeType.REQUEST,
                                                        action="approved") 
            borrow_request.update(status=RequestStatus.APPROVED)
            borrow_request.save()
        else:
            messages.error(request, 'Request could not be approved.')  

    return  redirect('view_requests')



@login_required
def deny_borrow_request(request, br_id):
    """
    Deny tool borrow request
    """
    borrow_request  = get_object_or_404(BorrowRequest, pk=br_id)
    # check if user is recipient of the borrow request
    if borrow_request.recipient == request.user:
        tool = get_object_or_404(Tool, pk=borrow_request.tool.id);
        # check if owner of tool is the recipient of the borrow request
        if tool.owner == request.user:
            # notify requester that the request was denied
            Notification.objects.create(recipient=borrow_request.sender, 
                                                        sender=request.user,
                                                        tool=tool,
                                                        notice_type=NoticeType.REQUEST,
                                                        action="denied") 
            borrow_request.update(status=RequestStatus.DENIED)
            borrow_request.save()
        else:
            messages.error(request, 'Request could not be denied.')  
    return  redirect('view_requests')

@login_required
def sender_cancel_request(request, br_id):
    """
    Cancel the borrow request if it is pending.
    """
    borrow_request  = get_object_or_404(BorrowRequest, pk=br_id)
    if borrow_request.sender== request.user and borrow_request.status == RequestStatus.PENDING:
        borrow_request.update(status=RequestStatus.CANCELED)
        borrow_request.save()
        Notification.objects.create(recipient=borrow_request.recipient, 
                                                    sender=request.user,
                                                    tool=borrow_request.tool,
                                                    notice_type=NoticeType.REQUEST,
                                                    action="canceled") 
    else:
        messages.error(request, 'Request cannot be canceled.')
    return redirect('view_requests')

@login_required
def sender_delete_request(request, br_id):
    """
    Set s_deleted to true. The borrow request will no longer appear in the user's 'sent requests' list
    - If s_deleted and r_deleted are both true, then the borrow request will be
    deleted. 
    """
    borrow_request  = get_object_or_404(BorrowRequest, pk=br_id)
    if borrow_request.recipient == request.user:
        if borrow_request.r_deleted:
            borrow_request.delete()
        else:
            borrow_request.update(s_deleted=True)
            borrow_request.save()
    else:
        messages.error(request, 'Request could not be deleted.')  
    return  redirect('view_requests')

@login_required
def recipient_delete_request(request, br_id):
    """
    Set r_deleted to true. The borrow request will no longer appear in the user's 'recieved requests' list
    - If s_deleted and r_deleted are both true, then the borrow request will be
    deleted. 
    """
    borrow_request  = get_object_or_404(BorrowRequest, pk=br_id)
    if borrow_request.recipient == request.user:
        if borrow_request.s_deleted:
            borrow_request.delete()
        else:
            borrow_request.update(r_deleted=True)
            borrow_request.save()
    else:
        messages.error(request, 'Request could not be deleted.')  
    return  redirect('view_requests')