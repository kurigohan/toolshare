from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.
def create_tool(request, template_name='tools/create_tool.html'):
    """
    Takes form information from request and adds to
    tool database.
    """
    return render

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

def tool_detail(request, template_name='tool_detail.html'):
    """
    Pulls tool from list, displays information about the tool.
    """
