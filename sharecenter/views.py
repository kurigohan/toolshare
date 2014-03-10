from django.shortcuts import render, redirect,get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from sharecenter.forms import ToolCreateForm
from sharecenter.models import Tool, Shed
from django.http import Http404, HttpResponseRedirect

@login_required
def create_tool(request, template_name='tools/create_tool.html'):
    """
    Create a new tool with data from request and add it to database.
    """
    if request.method == 'POST':
        form = ToolCreateForm(data=request.POST)
        if form.is_valid():
            user_profile = request.user.get_profile()
            tool = Tool(
                name=form.cleaned_data['name'],
                category=form.cleaned_data['category'],
                description=form.cleaned_data['description'],
                owner=user_profile,
                shed=user_profile.shed_owned.all()[0]
            )
            tool.save()
            url = reverse('tool_detail', kwargs={'tool_id':tool.id})
            return HttpResponseRedirect(url)
    else: 
        form = ToolCreateForm()

    return render(request, template_name, {'form': form})#no tool created
create_tool = login_required(create_tool)

@login_required
def my_tools(request, template_name='tools/my_tools.html'):
    """
    Display a table containing the user's tools. 
    """
    user = request.user.get_profile()
    tool_list = user.tool_owned.all()
    borrow_list = Tool.objects.filter(borrower=user.id)
    return render(request, template_name, {'tool_list':tool_list, 'borrow_list':borrow_list})
my_tools = login_required(my_tools)

@login_required
def edit_tool(request, tool_id, template_name='tools/edit_tool.html'):
    """
    Update tool info with data from request
    """
    tool=get_object_or_404(Tool, pk=tool_id)
    if request.user == tool.owner.user:
        if request.method == 'POST':
            form = ToolCreateForm(data=request.POST, instance=tool)
            if form.is_valid:  
                form.save()
                url = reverse('tool_detail', kwargs={'tool_id':tool.id})
                return HttpResponseRedirect(url)
        else:
            form = ToolCreateForm(instance=tool)
        return render(request, template_name, {'form':form}) #no editing done
    else:
        raise Http404 #can only edit own tools
edit_tool = login_required(edit_tool)

@login_required
def borrow_tool(request, tool_id):
    """
    Set selected tool as borrowed
    """
    tool = get_object_or_404(Tool, pk=tool_id)
    if tool.is_available():
        tool.borrow_tool(request.user.get_profile())
        tool.save()
    url = reverse('tool_detail', kwargs={'tool_id':tool.id})
    return HttpResponseRedirect(url)
borrow_tool = login_required(borrow_tool)

@login_required
def return_tool(request, tool_id):
    """
    Set selected tool as returned
    """
    tool = get_object_or_404(Tool, pk=tool_id)
    if tool.borrower.user == request.user:
        tool.return_tool()
        tool.save()
    url = reverse('tool_detail', kwargs={'tool_id':tool.id})
    return HttpResponseRedirect(url)
return_tool = login_required(return_tool)

@login_required
def tool_detail(request,  tool_id, template_name='tools/tool_detail.html'):
    """
    Display tool info
    """
    tool = get_object_or_404(Tool, pk=tool_id)
    return render(request, template_name, {'tool':tool})
tool_detail = login_required(tool_detail)

@login_required
def my_sheds(request, template_name='sheds/my_sheds.html'):
    """
    Display table containing user's sheds. 
    """
    shed_list = request.user.get_profile().shed_owned.all()
    return render(request, template_name, {'shed_list':shed_list})
my_sheds = login_required(my_sheds)

@login_required
def shed_detail(request, shed_id, template_name='sheds/shed_detail.html'):
    """
    Display shed info, tool list as table
    """
    shed = get_object_or_404(Shed, pk=shed_id)
    tool_list = shed.shed_tools.all()
    return render(request, template_name, {'shed':shed, 'tool_list':tool_list})
shed_detail = login_required(shed_detail)

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
    shed_list = Shed.objects.filter(postal_code=request.user.get_profile().postal_code)
    return render(request, template_name, {'shed_list':shed_list})

share_zone = login_required(share_zone)
