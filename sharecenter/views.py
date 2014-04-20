from django.shortcuts import render, redirect,get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from sharecenter.forms import ToolCreateForm
from sharecenter.models import Tool, Shed

from notifications.models import Notification
import notifications.NoticeType as NoticeType

from borrow_requests.models import BorrowRequest
import borrow_requests.RequestStatus as RequestStatus

@login_required
def create_tool(request, template_name='tools/create_tool.html'):
    """
    Create a new tool with data from request and add it to database.
    """
    if request.method == 'POST':
        form = ToolCreateForm(request.POST, request.FILES)
        if form.is_valid():
            shed = request.user.shed_owned.all()[0]
            request.FILES['image'].name=str(request.user.username+form.cleaned_data['name'])+'.png'
          #  form.clean_image()
            tool = Tool(
                name=form.cleaned_data['name'],
                category=form.cleaned_data['category'],
                description=form.cleaned_data['description'],
                owner=request.user,
                shed=shed,
                image=request.FILES['image']
            )
            tool.save()
            activity_msg = "added %s to %s" % (tool.name, tool.shed.name)
            Notification.objects.create(recipient=request.user, 
                                                    sender=request.user,
                                                    notice_type=NoticeType.ACTIVITY,
                                                    message=activity_msg)                                        
            url = reverse('tool_detail', kwargs={'tool_id':tool.id})
            return HttpResponseRedirect(url)
    else: 
        form = ToolCreateForm()

    return render(request, template_name, {'form': form})

@login_required
def delete_tool(request, tool_id):
    tool = get_object_or_404(Tool, pk=tool_id)
    if request.user == tool.owner and tool.is_available():
        activity_msg = "deleted %s from %s" % (tool.name, tool.shed.name)
        tool.delete()
        Notification.objects.create(recipient=request.user, 
                                                sender=request.user,
                                                notice_type=NoticeType.ACTIVITY,
                                                message=activity_msg)         
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
    if request.user != tool.owner and tool.is_available():
        # send borrow request
        BorrowRequest.objects.create(recipient=tool.owner, sender=request.user, tool=tool)
        # send notification to tool owner
        Notification.objects.create(recipient=tool.owner, 
                                                        sender=request.user,
                                                        tool=tool,
                                                        notice_type=NoticeType.REQUEST,
                                                        action="borrow")                            

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
    # send notification to tool owner
    Notification.objects.create(recipient=tool.owner, 
                                            sender=request.user,
                                            tool=tool,
                                            notice_type=NoticeType.ALERT,
                                            action="returned")                            

    url = reverse('tool_detail', kwargs={'tool_id':tool.id})
    return HttpResponseRedirect(url)

@login_required
def tool_detail(request,  tool_id, template_name='tools/tool_detail.html'):
    """
    Display tool info
    """
    tool = get_object_or_404(Tool, pk=tool_id)
    permissions = {"borrow": False, "return":False, "delete":False, "edit":False}
    if request.user == tool.owner:
        permissions["edit"] = True
        if tool.is_available(): #tool cannot be deleted if its borrowed
            permissions["delete"] = True
    elif tool.shed.postal_code == request.user.profile.postal_code:
        if not tool.is_available() and tool.borrower == request.user:
            permissions["return"] = True
        else:
            #check if the the user has a pending borrow request for the tool
            has_request = (BorrowRequest.objects.filter(sender=request.user, tool=tool,
                                                    status=RequestStatus.PENDING).count() > 0)
            if not has_request:
                permissions["borrow"] = True
    return render(request, template_name, {'tool':tool, 'permissions':permissions})

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

@login_required
def create_shed(request, template_name='sheds/create_shed.html'):
    """
    Create a new shed with data from request and add it to database.
    """
    
    if request.method == 'POST':
        form = ShedCreateForm(data=request.POST)
        if form.is_valid():
            shed = Shed(
                name=form.cleaned_data['name'],
                street=form.cleaned_data['street'],
                state=form.cleaned_data['state'],
                postal_code = form.cleaned_data['postal_code'],
                owner=request.user,
                
            )
            shed.save()
                            
            url = reverse('shed_detail', kwargs={'shed_id':shed.id})
            return HttpResponseRedirect(url)
    else: 
        form = ShedCreateForm()

    return render(request, template_name, {'form': form})


@login_required
def delete_shed(request, shed_id):
    shed = get_object_or_404(Shed, pk=shed_id)
    if request.user == shed.owner and shed.share_count() == 0 and request.user.shed_owned.all().count() > 1:
        shed.delete();
        activity_msg = "deleted %s" % (shed.name,)
        Notification.objects.create(recipient=request.user, 
                                                sender=request.user,
                                                notice_type=NoticeType.ACTIVITY,
                                                message=activity_msg)
    return redirect('my_sheds')

@login_required
def share_zone(request, template_name='sheds/share_zone.html'):
    """
    Display table with all sheds in share zone
    """
    shed_list = Shed.objects.filter(postal_code=request.user.profile.postal_code)
    return render(request, template_name, {'shed_list':shed_list})




