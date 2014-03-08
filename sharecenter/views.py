from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.
def create_tool(request):
    name=request.POST['tool_name']
    description=request.POST['description']
    category=request.POST['category']
    owner=request.user.id
    return #url that requested page

def my_tools(request, template_name='my_tools.html'):
    """
    Calls the full list of tools and pulls only the tools with an
    owner id that matches the user making the request.
    """
    return render_to_response

def edit_tool(request, template_name='tools/edit_tool.html'):
    """
    Takes form information from request, updates tool and updates
    tool database.
    """
    return render

def tool_detail(request, tool_id):
    tool=get_object_or_404(ToolModel, pk=tool_id)
    return render(tool)
