from django.shortcuts import render, redirect,get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from sharecenter.forms import ToolCreateForm
from sharecenter.models import Tool, Shed
from django.http import Http404  

# Create your views here.
def create_tool(request, template_name='tools/create_tool.html'):
    if request.method == 'POST':
        form = ToolCreateForm(data=request.POST)
        if form.is_valid():
          #  tool_obj = form.save(commit=False)
          #  tool_obj.owner = request.user.get_profile()
           # tool_obj.save()
            user_profile = request.user.get_profile()
            tool = Tool.objects.create_tool(
                name=form.cleaned_data['name'],
                category=form.cleaned_data['category'],
                description=form.cleaned_data['description'],
                owner=user_profile,
                shed=user_profile.shed_owned.all()[0]
            )
            tool.save()
            return redirect('my_tools')
    else: 
        form = ToolCreateForm()

    return render(request, template_name, {'form': form})

def my_tools(request, template_name='tools/my_tools.html'):
    """
    Display a table containing the user's tools. 
    """
    tool_list = request.user.get_profile().tool_owned.all()

    return render(request, template_name, {'tool_list':tool_list})

def edit_tool(request, tool_id, template_name='tools/edit_tool.html'):
    tool=get_object_or_404(Tool, pk=tool_id)
    if request.user == tool.owner:
        if request.method == 'POST':
            form = ToolCreateForm(data=request.POST, instance=tool)
            if form.is_valid:
              
                form.save()
            return redirect('my_tools')
        else:
            form = ToolCreateForm(instance=tool)
        return render(request, template_name, {'form':form})
    else:
        raise Http404

def borrow_tool(request, tool_id):
    tool = get_object_or_404(Tool, pk=tool_id)
    if tool.is_available():
        tool.borrow_tool(request.user.get_profile())
        tool.save()
    return redirect('my_sheds')


def tool_detail(request,  tool_id, template_name='tools/tool_detail.html'):
    tool = get_object_or_404(Tool, pk=tool_id)
    return render(request, template_name, {'tool':tool})



def my_sheds(request, template_name='sheds/my_sheds.html'):
    """
    Display table containing user's sheds. 
    """
    shed_list = request.user.get_profile().shed_owned.all()
    return render(request, template_name, {'shed_list':shed_list})

def shed_detail(request, shed_id, template_name='sheds/shed_detail.html'):
    shed = get_object_or_404(Shed, pk=shed_id)
    tool_list = shed.shed_tools.all()
    return render(request, template_name, {'shed':shed, 'tool_list':tool_list})

def create_shed(request, template_name='sheds/create_shed.html'):
    if request.method == 'POST':
        shed = ShedCreateForm(data=request.POST);
        shed.owner = request.user.id;
        shed.toolLimit = request.toolLimit;
        shed.save();
        return redirect('user_home')
    else:
        form = ShedCreateForm()
        
    return render(request, template_name, {'form': form})

def edit_shed(request, shed_id, template_name='sheds/edit_shed.html'):
    shed = get_object_or_404(Shed,pk=shed_id);
    if request.method == 'POST':
        shed.name = request.POST['name']
        shed.owner = request.user
        shed.toolLimit = request.toolLimit
        shed.state = request.POST['state']
        shed.zipcode=request.POST['postal_code']
        shed.street=request.POST['postal_code']
        shed.save();
    return render(request, template_name, {'shed':shed})



def share_zone(request, template_name='sheds/share_zone.html'):
    shed_list = Shed.objects.filter(postal_code=request.user.get_profile().postal_code)
    return render(request, template_name, {'shed_list':shed_list})
