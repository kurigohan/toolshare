from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def create_tool(request, template_name='tools/create_tool.html'):
    if request.method == 'POST':
        form = ToolCreationForm(data=request.POST)
        if form.is_valid():
            tool_obj = form.save(commit=False)
            tool_obj.owner = request.user
            tool_obj.save()
            return redirect(reverse('user_home'))
    else: 
        form = ToolCreationForm()

    return render(request, template_name, {'form': form})

def my_tools(request, template_name='my_tools.html'):
    """
    Calls the full list of tools and pulls only the tools with an
    owner id that matches the user making the request.
    """
    return render_to_response

def edit_tool(request, tool_id, template_name='tools/edit_tool.html'):
    tool=get_object_or_404(ToolModel, pk=tool_id)
    if request.method == 'POST':
        tool.name=request.POST['tool_name']
        tool.description=request.POST['description']
        tool.category=request.POST['category']
        tool.save()
        #return redirect to success page
    return render(request, template_name)


def tool_detail(request, tool_id):
    tool=get_object_or_404(ToolModel, pk=tool_id)
    return render(tool)


def create_shed(request, template_name='sheds/create_shed.html'):
    if request.method == 'POST':
        shed1 = ShedCreateForm(data=request.POST);
        shed1.owner = request.user.id;
        shed1.toolLimit = request.toolLimit;
        shed1.save();
        return redirect(reverse('user_home'))
    else:
        form = ShedCreateForm()
        
    return render(request, template_name, {'form': form});

def edit_shed(request, shed_id, template_name='sheds/edit_shed.html'):
    shed1=get_object_or_404(ShedModel,pk=shed_id);
    if request.method == 'POST':
        shed1.name = request.POST['name'];
        shed1.owner = request.user.id;
        shed1.toolLimit = request.toolLimit;
        shed1.state = request.POST['state'];
        shed1.zipcode=request.POST['zipcode'];
        shed1.street=request.POST['zipcode'];
        shed1.save();
    return render(request, template_name);

def shed_detail(request):
    shed1=get_object_or_404(ShedModel,pk=request.SHEDID);
    return render(request,template_name='sheds/shed_detail.html',shed1);
