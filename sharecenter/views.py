from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from sharecenter.forms import ToolCreationForm

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
<<<<<<< HEAD

=======
>>>>>>> 4d29bb7adeef6194033da3bc690101b2d9eb7b92

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
    return False


def create_shed(request):
    shed1 = shed();
    shed1.name = request.name;
    shed1.owner = request.user.id;
    shed1.toolLimit = request.toolLimit;
    address1 = address();
    address1.state = request.state;
    address1.zipcode=request.zipcode;
    address1.street=request.street;
    address1.save();
    shed1.address=address1.id;
    shed1.save();
    return False

def edit_shed(request):
    shed1=get_object_or_404(ShedModel,pk=request.SHEDID);
    shed1.name = request.name;
    shed1.owner = request.user.id;
    shed1.toolLimit = request.toolLimit;
    address1 = address();
    address1.state = request.state;
    address1.zipcode=request.zipcode;
    address1.street=request.street;
    address1.save();
    shed1.address=address1.id;
    shed1.save();
    return render(request,template_name='sheds/edit_shed.html');

#def shed_detail(request):
  #  shed1=get_object_or_404(ShedModel,pk=request.SHEDID);
    #return render(request,template_name='sheds/shed_detail.html',shed1);
