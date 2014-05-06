from django.shortcuts import render, redirect,get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.db.models import Q
from django.contrib import messages

from sharecenter.forms import ToolForm,  ShedForm
from sharecenter.models import Tool, Shed

from notifications.models import Notification, Activity
import notifications.NoticeType as NoticeType

from borrow_requests.models import BorrowRequest
import borrow_requests.RequestStatus as RequestStatus

from profiles.models import UserProfile

import os
@login_required
def create_tool(request, template_name='tools/create_tool.html'):
    """
    Create a new tool with data from request and add it to database.
    """
    if request.method == 'POST':
        form = ToolForm(request.user, request.POST, request.FILES)
        if form.is_valid():
         #   form.clean_image()
          #  shed = request.user.shed_owned.all()[0]
            image = None
            if form.cleaned_data['image']:
                image = form.cleaned_data['image']
            tool = Tool(
                name=form.cleaned_data['name'],
                category=form.cleaned_data['category'],
                description=form.cleaned_data['description'],
                owner=request.user,
                shed=form.cleaned_data['shed'],
                image=image
            )
            tool.save()
            if image:
                tool.image.name = rename_file(tool)
                tool.save()
            activity_msg = "Added %s to %s" % (tool.name, tool.shed.name)
            Activity.objects.create(user=request.user, message=activity_msg)                                 
            url = reverse('tool_detail', kwargs={'tool_id':tool.id})
            return HttpResponseRedirect(url)
    else: 
        form = ToolForm(request.user)

    return render(request, template_name, {'form': form})

@login_required
def delete_tool(request, tool_id):
    tool = get_object_or_404(Tool, pk=tool_id)
    if request.user == tool.owner and tool.is_available():
        if tool.image:
            try:
                os.remove(tool.image.path) # remove image
            except: pass

        activity_msg = "Deleted %s from %s" % (tool.name, tool.shed.name)
        Activity.objects.create(user=request.user,
                                                message=activity_msg)     
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
            if not request.POST.get('shed'): # set tool to previous shed if none selected
                request.POST = request.POST.copy()
                request.POST['shed'] = tool.shed.id
            form = ToolForm(request.user, request.POST, request.FILES, instance=tool)
            if form.is_valid():
                form.save()
                url = reverse('tool_detail', kwargs={'tool_id':tool.id})
                return HttpResponseRedirect(url)
        else:
            form = ToolForm(user=request.user, instance=tool)
        return render(request, template_name, {'form':form, 'tool':tool}) #no editing done
    else:
        url = reverse('tool_detail', kwargs={'tool_id':tool.id})
        return HttpResponseRedirect(url)



@login_required
def create_tool_to_shed(request, shed_id ,template_name='tools/create_tool.html'):
    """
    Create a new tool with the specified shed selected by default in the form.
    """
    shed = get_object_or_404(Shed, pk=shed_id)
    if request.method == 'POST':
        form = ToolForm(request.user, request.POST, request.FILES)
        image = None
        if form.is_valid():
            if form.cleaned_data['image']:
                image = form.cleaned_data['image']
            tool = Tool(
                name=form.cleaned_data['name'],
                category=form.cleaned_data['category'],
                description=form.cleaned_data['description'],
                owner=request.user,
                shed=shed,
                image=image,
            )
            tool.save()
            if image:
                tool.image.name = rename_file(tool)
                tool.save()
            activity_msg = "Added %s to %s" % (tool.name, tool.shed.name)
            Activity.objects.create(user=request.user,
                                                    message=activity_msg)                               
            url = reverse('tool_detail', kwargs={'tool_id':tool.id})
            return HttpResponseRedirect(url)
    else: 
        form = ToolForm(user=request.user, initial={'shed':shed})
    return render(request, template_name, {'form': form})

@login_required
def borrow_tool(request, tool_id):
    """
    Send a borrow request for the tool
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
        messages.success(request, "Borrow request sent.")
        activity_msg = "Sent a borrow request for %s to %s" % (tool.name, tool.owner.username)
        Activity.objects.create(user=request.user,
                                                message=activity_msg)     
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
    activity_msg = "Returned %s to %s" % (tool.name, tool.shed.name)
    Activity.objects.create(user=request.user,
                                                message=activity_msg)     
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
    permissions = {'delete':False, 'edit':False, 'add_tool':False, 'set_home':False}
    if request.user == shed.owner:
        permissions['edit'] = permissions['add_tool'] = True
        if request.user.profile.home_shed != shed:
            permissions['set_home'] = True
        if shed.share_count() == 0 and request.user.profile.home_shed != shed:
            permissions['delete'] = True

    return render(request, template_name, {'shed':shed, 'tool_list':tool_list, 'permissions':permissions})

@login_required
def create_shed(request, template_name='sheds/create_shed.html'):
    """
    Create a new shed with data from request and add it to database.
    """
    
    if request.method == 'POST':
        form = ShedForm(request.POST, request.FILES)
        if form.is_valid():
            image = None
            if form.cleaned_data['image']:
                image=form.cleaned_data['image']
            shed = Shed(
                name=form.cleaned_data['name'],
                street=form.cleaned_data['street'],
                city=form.cleaned_data['city'],
                state=form.cleaned_data['state'],
                postal_code = form.cleaned_data['postal_code'],
                owner=request.user,
                image=image,
            )
            shed.save()
            if image:
                shed.image.name = rename_file(shed)
                shed.save()
            activity_msg = "Created a new shed (%s)" % (shed.name,)
            Activity.objects.create(user=request.user,
                                                    message=activity_msg)     
            url = reverse('shed_detail', kwargs={'shed_id':shed.id})
            return HttpResponseRedirect(url)
    else: 
        form = ShedForm(initial={'state':'NY'})

    return render(request, template_name, {'form': form})


@login_required
def delete_shed(request, shed_id):
    shed = get_object_or_404(Shed, pk=shed_id)
    if request.user == shed.owner and shed.share_count() == 0 \
                                 and request.user.profile.home_shed != shed:
        if shed.image:
            try:
                os.remove(shed.image.path) # remove image
            except: pass
        activity_msg = "Deleted a shed (%s)" % (shed.name,)
        Activity.objects.create(user=request.user,
                                                message=activity_msg)
        shed.delete();

    return redirect('my_sheds')

@login_required
def edit_shed(request, shed_id, template_name='sheds/edit_shed.html'):
    """
    Update shed info with data from request
    """
    shed = get_object_or_404(Shed, pk=shed_id)
    if request.user == shed.owner:
        if request.method == 'POST':
            form = ShedForm(request.POST, request.FILES, instance=shed)
            if form.is_valid():  
                form.save()
                url = reverse('shed_detail', kwargs={'shed_id':shed.id})
                return HttpResponseRedirect(url)
        else:
            form = ShedForm(instance=shed)
        return render(request, template_name, {'form':form, 'shed':shed}) #no editing done
    else:
        url = reverse('shed_detail', kwargs={'shed_id':shed.id})
        return HttpResponseRedirect(url)


@login_required
def set_home_shed(request, shed_id):
    shed = get_object_or_404(Shed, pk=shed_id)
    if request.user == shed.owner:
        request.user.profile.home_shed = shed
        request.user.profile.save()
        activity_msg = "Set %s as home shed" % (shed.name,)
        Activity.objects.create(user=request.user,
                                                message=activity_msg)     
    url = reverse('shed_detail', kwargs={'shed_id':shed.id})
    return HttpResponseRedirect(url)

@login_required
def share_zone(request, template_name='community/share_zone.html'):
    """
    Display table with all sheds in share zone
    """

    results = Tool.objects.filter(shed__postal_code=request.user.profile.postal_code)
    results = results.exclude(owner=request.user)
  #  if request.method == 'GET' and 'q' in request.GET:
    if request.method == 'GET' and 'q' in request.GET:
        search_term = request.GET.get('q', False)
        results = results.filter(Q(name__icontains=search_term))
    stats = get_community_stats( request.user )
    return render(request, template_name, {'results':results, 'stats':stats})

def get_community_stats( user ):
    """
    Returns the profile of the most active borrower and lender for the user's share zone
    """
    profile_list = UserProfile.objects.filter(home_shed__postal_code=user.profile.postal_code)
    most_active_borrower = profile_list[0]
    most_active_lender = profile_list[0]
    for p in profile_list:
        if p.stats.total_borrowed > most_active_borrower.stats.total_borrowed:
            most_active_borrower = p
        if p.stats.total_shared > most_active_lender.stats.total_shared:
            most_active_lender = p
    stats = { 'most_active_borrower' : most_active_borrower, 'most_active_lender': 
                                                                                most_active_lender }
    return stats


def rename_file( instance ):
    name, ext = os.path.splitext(instance.image.path)
    name = name + '_' + str(instance.pk) + ext # add primary key (id) to name
    try:
        os.rename(instance.image.path, name)
    except: 
        name = None
    instance.image.name = name
    instance.save()
    return name