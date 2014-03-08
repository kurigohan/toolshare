from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.
def create_tool(request):
    name=request.POST['tool_name']
    description=request.POST['description']
    category=request.POST['category']
    owner=request.user.id
    return render(request,template_name='tools/create_tool.html')

def my_tools(request):
    toolList = request.user.profile.tool_set()
    return render(request,template_name='tools/my_tools.html',{'tool':tool,toolList})

def edit_tool(request):
    name=request.POST['tool_name']
    description=request.POST['description']
    category=request.POST['category']
    return render(request,template_name='tools/edit_tool.html')

def tool_detail(request, tool_id):
    tool=get_object_or_404(ToolModel, pk=tool_id)
    return render(request,template_name='tools/tool_detail.html',tool)
