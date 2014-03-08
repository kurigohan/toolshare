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

    return render(template_name, {'form': form})

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
