[1mdiff --git a/profiles/urls.py b/profiles/urls.py[m
[1mindex b6545c8..95a4001 100644[m
[1m--- a/profiles/urls.py[m
[1m+++ b/profiles/urls.py[m
[36m@@ -28,17 +28,17 @@[m [mfrom profiles import views as ProfileView[m
 [m
 [m
 urlpatterns = patterns('',[m
[31m-                    #   url(r'^create/$',[m
[31m-                        #   ProfileView.create_profile,[m
[31m-                         #  name='profiles_create_profile'),[m
[31m-                      # url(r'^edit/$',[m
[31m-                     #      ProfileView.edit_profile,[m
[31m-                         #  name='profiles_edit_profile'),[m
[32m+[m[32m                       url(r'^create/$',[m
[32m+[m[32m                           ProfileView.create_profile,[m
[32m+[m[32m                           name='profiles_create_profile'),[m
[32m+[m[32m                       url(r'^edit/$',[m
[32m+[m[32m                           ProfileView.edit_profile,[m
[32m+[m[32m                           name='profiles_edit_profile'),[m
                        url(r'^(?P<username>\w+)/$',[m
                            ProfileView.profile_detail,[m
                            name='profiles_profile_detail'),[m
[31m-                       #url(r'^$',[m
[31m-                          # ProfileView.profile_list,[m
[31m-                           #name='profiles_profile_list'),[m
[32m+[m[32m                       url(r'^$',[m
[32m+[m[32m                           ProfileView.profile_list,[m
[32m+[m[32m                           name='profiles_profile_list'),[m
 [m
                        )[m
[1mdiff --git a/sharecenter/models.py b/sharecenter/models.py[m
[1mindex abf784f..7fca042 100644[m
[1m--- a/sharecenter/models.py[m
[1m+++ b/sharecenter/models.py[m
[36m@@ -37,7 +37,7 @@[m [mclass ShedModel(models.Model):[m
     name = models.charField(max_length=30);[m
     owner = models.ForeignKey(UserProfile);[m
     toolLimit = models.IntegerField(verbose_name='tool limit');[m
[31m-    address = models.OneToOneField(Address, related_name='address');[m
[32m+[m[32m    address = models.OneToOne(Address, related_name='address');[m
 [m
     def addTool(tool):[m
         tool.shed = self.id;[m
[1mdiff --git a/sharecenter/tools/forms.py b/sharecenter/tools/forms.py[m
[1mdeleted file mode 100644[m
[1mindex 5a212e3..0000000[m
[1m--- a/sharecenter/tools/forms.py[m
[1m+++ /dev/null[m
[36m@@ -1,13 +0,0 @@[m
[31m-[m
[31m-from django import forms[m
[31m-from django.db import models[m
[31m-from django.forms import ModelForm[m
[31m-[m
[31m- [m
[31m-class ToolCreationForm(forms.Form):[m
[31m-    """[m
[31m-    Form for editting account info.[m
[31m-    """[m
[31m-    name = forms.CharField(label='Name', max_length=30, widget=forms.TextInput(attrs={'class':'form-control,form-group,input-single','placholder':'Name of Tool'}))error_messages={'required': 'No tool name entered.'})[m
[31m-    category = forms.CharField(label='Category', max_length=30, widget=forms.TextInput(attrs={'class':'form-control,form-group,input-single','placeholder':'Category of Tool'})error_messages={'required': 'No category was entered.'})[m
[31m-    description = forms.CharField(label='Description', max_length=250, widget=forms.TextInput(attrs={'class':'form-control,form-group,input-single','placeholder':'Category of Tool'})error_messages={'required': 'No description was entered.'})[m
\ No newline at end of file[m
[1mdiff --git a/sharecenter/views.py b/sharecenter/views.py[m
[1mindex 60d0bff..7d91544 100644[m
[1m--- a/sharecenter/views.py[m
[1m+++ b/sharecenter/views.py[m
[36m@@ -1,69 +1,26 @@[m
 from django.shortcuts import render[m
[31m-from django.shortcuts import redirect[m
[31m-from django.contrib.auth.decorators import login_required[m
[32m+[m[32mfrom django.shortcuts import render_to_response[m
 [m
 # Create your views here.[m
[31m-def create_tool(request, template_name='tools/create_tool.html'):[m
[31m-    if request.method == 'POST':[m
[31m-        form = ToolCreationForm(data=request.POST)[m
[31m-        if form.is_valid():[m
[31m-            tool_obj = form.save(commit=False)[m
[31m-            tool_obj.owner = request.user[m
[31m-            tool_obj.save()[m
[31m-            return redirect(reverse('user_home'))[m
[31m-    else: [m
[31m-        form = ToolCreationForm()[m
[32m+[m[32mdef create_shed(request, template_name='sheds/create_shed.html'):[m
 [m
[31m-    return render(template_name, {'form': form})[m
[32m+[m[32m    #Create shed with info from request[m
 [m
[31m-def my_tools(request, template_name='my_tools.html'):[m
[31m-    """[m
[31m-    Calls the full list of tools and pulls only the tools with an[m
[31m-    owner id that matches the user making the request.[m
[31m-    """[m
[31m-    return render_to_response[m
[32m+[m[32mdef my_shed(request, template_name='sheds/my_shed.html'):[m
 [m
[31m-def edit_tool(request, tool_id):[m
[31m-    tool=get_object_or_404(ToolModel, pk=tool_id)[m
[31m-    tool.name=request.POST['tool_name'][m
[31m-    tool.description=request.POST['description'][m
[31m-    tool.category=request.POST['category'][m
[31m-    return render(request,template_name='tools/edit_tool.html')[m
[32m+[m[32m    #temporary template name; render list of tools in shed[m
 [m
[32m+[m[32mdef edit_shed(request,template_name='sheds/edit_shed.html'):[m
[32m+[m[32m    #temporary profile name;[m[41m [m
 [m
[31m-def tool_detail(request, tool_id):[m
[31m-    tool=get_object_or_404(ToolModel, pk=tool_id)[m
[31m-    return render(tool)[m
[31m-[m
[31m-[m
[31m-def create_shed(request):[m
[31m-    shed1 = shed();[m
[31m-    shed1.name = request.name;[m
[31m-    shed1.owner = request.user.id;[m
[31m-    shed1.toolLimit = request.toolLimit;[m
[31m-    address1 = address();[m
[31m-    address1.state = request.state;[m
[31m-    address1.zipcode=request.zipcode;[m
[31m-    address1.street=request.street;[m
[31m-    address1.save();[m
[31m-    shed1.address=address1.id;[m
[31m-    shed1.save();[m
[32m+[m[32mdef kill_shed(request,shed,template_name='sheds/delete_shed.html'):[m
[32m+[m[41m    [m
     return render;[m
[32m+[m[32m    #temporary profile name; remove shed from table[m
 [m
[31m-def edit_shed(request):[m
[31m-    shed1=get_object_or_404(ShedModel,pk=request.SHEDID);[m
[31m-    shed1.name = request.name;[m
[31m-    shed1.owner = request.user.id;[m
[31m-    shed1.toolLimit = request.toolLimit;[m
[31m-    address1 = address();[m
[31m-    address1.state = request.state;[m
[31m-    address1.zipcode=request.zipcode;[m
[31m-    address1.street=request.street;[m
[31m-    address1.save();[m
[31m-    shed1.address=address1.id;[m
[31m-    shed1.save();[m
[31m-    return render(request,template_name='sheds/edit_shed.html');[m
[32m+[m[32mdef shed_detail(request,shed,template_name='shed/shed_detail.html'):[m
[32m+[m[32m    return(render(get_object_or_404(ShedModel,pk=shed)));[m
[32m+[m[32m    #temporary profile name ; render shed info[m
 [m
[31m-def shed_detail(request):[m
[31m-    shed1=get_object_or_404(ShedModel,pk=request.SHEDID);[m
[31m-    return render(request,template_name='sheds/shed_detail.html',shed1);[m
[32m+[m[32mdef[m[41m [m
[41m+    [m
[1mdiff --git a/static/css/tablecloth.css b/static/css/tablecloth.css[m
[1mdeleted file mode 100644[m
[1mindex 4d7dc62..0000000[m
[1m--- a/static/css/tablecloth.css[m
[1m+++ /dev/null[m
[36m@@ -1,352 +0,0 @@[m
[31m-.table th.center, .table td.center  { text-align:center; }[m
[31m-.table th.right, .table td.right    { text-align:right; }[m
[31m-[m
[31m-.table th.headerSortable:hover {[m
[31m-  cursor:pointer;[m
[31m-}[m
[31m-.table th.headerSortDown {[m
[31m-  background-image: url('../img/asc.gif');[m
[31m-  cursor: pointer;[m
[31m-  background-repeat: no-repeat;[m
[31m-  background-position: center right;[m
[31m-  padding-right:16px !important;[m
[31m-}[m
[31m-.table th.headerSortUp {[m
[31m-  background-image: url('../img/desc.gif');[m
[31m-  cursor: pointer;[m
[31m-  background-repeat: no-repeat;[m
[31m-  background-position: center right;[m
[31m-  padding-right:16px !important;[m
[31m-}[m
[31m-[m
[31m-.table tr.highlight td,         .table tr.highlight:hover td,[m
[31m-.table td.highlight,            .table td.highlight:hover             { background:#FFF9D7 !important; }[m
[31m-.table tr.highlight-primary td, .table tr.highlight-primary:hover td,[m
[31m-.table td.highlight-primary,    .table td.highlight-primary:hover     { background:#0074cc !important; color:#FFF; }[m
[31m-.table tr.highlight-info td,    .table tr.highlight-info:hover td,[m
[31m-.table td.highlight-info,       .table td.highlight-info:hover        { background:#49afcd !important; color:#FFF; }[m
[31m-.table tr.highlight-success td, .table tr.highlight-success:hover td,[m
[31m-.table td.highlight-success,    .table td.highlight-success:hover     { background:#5bb75b !important; color:#FFF; }[m
[31m-.table tr.highlight-warning td, .table tr.highlight-warning:hover td,[m
[31m-.table td.highlight-warning,    .table td.highlight-warning:hover     { background:#faa732 !important; color:#FFF; }[m
[31m-.table tr.highlight-danger td,  .table tr.highlight-danger:hover td,[m
[31m-.table td.highlight-danger,     .table td.highlight-danger:hover      { background:#da4f49 !important; color:#FFF; }[m
[31m-.table tr.highlight-inverse td, .table tr.highlight-inverse:hover td,[m
[31m-.table td.highlight-inverse,    .table td.highlight-inverse:hover     { background:#414141 !important; color:#FFF; }[m
[31m-[m
[31m-/* DEFAULT THEME */[m
[31m-[m
[31m-.table caption {[m
[31m-  text-align:left;[m
[31m-  padding:10px 0;[m
[31m-}[m
[31m-[m
[31m-/* DARK THEME */[m
[31m-[m
[31m-.table-dark {[m
[31m-  width: 100%;[m
[31m-  margin-bottom: 18px;[m
[31m-  color:#CCC;[m
[31m-}[m
[31m-.table-dark caption {[m
[31m-  color:#FFF;[m
[31m-}[m
[31m-.table-dark th,[m
[31m-.table-dark td {[m
[31m-  padding: 8px;[m
[31m-  line-height: 18px;[m
[31m-  text-align: left;[m
[31m-  vertical-align: top;[m
[31m-  border-top: 1px solid #232323;[m
[31m-}[m
[31m-.table-dark th.headerSortable:hover {[m
[31m-  cursor:pointer;[m
[31m-}[m
[31m-.table-dark th.headerSortDown,[m
[31m-.table-dark th.headerSortUp {[m
[31m-  background-color:#000;[m
[31m-  background-image: url('../img/asc_light.gif');[m
[31m-  background-repeat: no-repeat;[m
[31m-  background-position: center right;[m
[31m-}[m
[31m-.table-dark th {[m
[31m-  font-weight: bold;[m
[31m-}[m
[31m-.table-dark thead th {[m
[31m-  background:#111;[m
[31m-  color:#E5E5E5;[m
[31m-  vertical-align: bottom;[m
[31m-}[m
[31m-.table-dark colgroup + thead tr:first-child th,[m
[31m-.table-dark colgroup + thead tr:first-child td,[m
[31m-.table-dark thead:first-child tr:first-child th,[m
[31m-.table-dark thead:first-child tr:first-child td {[m
[31m-  border-top: 0;[m
[31m-}[m
[31m-.table-dark tbody + tbody {[m
[31m-  border-top: 2px solid #232323;[m
[31m-}[m
[31m-.table-dark.table-condensed th,[m
[31m-.table-dark.table-condensed td {[m
[31m-  padding: 4px 5px;[m
[31m-}[m
[31m-.table-dark.table-bordered {[m
[31m-  border: 1px solid #232323;[m
[31m-  border-left: 0;[m
[31m-  border-collapse: separate;[m
[31m-  *border-collapse: collapsed;[m
[31m-  -webkit-border-radius: 4px;[m
[31m-  -moz-border-radius: 4px;[m
[31m-  border-radius: 4px;[m
[31m-}[m
[31m-.table-dark.table-bordered th,[m
[31m-.table-dark.table-bordered td {[m
[31m-  border-left: 1px solid #232323;[m
[31m-}[m
[31m-.table-dark.table-bordered thead:first-child tr:first-child th,[m
[31m-.table-dark.table-bordered tbody:first-child tr:first-child th,[m
[31m-.table-dark.table-bordered tbody:first-child tr:first-child td {[m
[31m-.table-dark  border-top: 0;[m
[31m-}[m
[31m-.table-dark.table-bordered thead:first-child tr:first-child th:first-child,[m
[31m-.table-dark.table-bordered tbody:first-child tr:first-child td:first-child {[m
[31m-  -webkit-border-radius: 4px 0 0 0;[m
[31m-  -moz-border-radius: 4px 0 0 0;[m
[31m-  border-radius: 4px 0 0 0;[m
[31m-}[m
[31m-.table-dark.table-bordered thead:first-child tr:first-child th:last-child,[m
[31m-.table-dark.table-bordered tbody:first-child tr:first-child td:last-child {[m
[31m-  -webkit-border-radius: 0 4px 0 0;[m
[31m-  -moz-border-radius: 0 4px 0 0;[m
[31m-  border-radius: 0 4px 0 0;[m
[31m-}[m
[31m-.table-dark.table-bordered thead:last-child tr:last-child th:first-child,[m
[31m-.table-dark.table-bordered tbody:last-child tr:last-child td:first-child {[m
[31m-  -webkit-border-radius: 0 0 0 4px;[m
[31m-  -moz-border-radius: 0 0 0 4px;[m
[31m-  border-radius: 0 0 0 4px;[m
[31m-}[m
[31m-.table-dark.table-bordered thead:last-child tr:last-child th:last-child,[m
[31m-.table-dark.table-bordered tbody:last-child tr:last-child td:last-child {[m
[31m-  -webkit-border-radius: 0 0 4px 0;[m
[31m-  -moz-border-radius: 0 0 4px 0;[m
[31m-  border-radius: 0 0 4px 0;[m
[31m-}[m
[31m-.table-dark.table-striped tbody tr:nth-child(odd) td,[m
[31m-.table-dark.table-striped tbody tr:nth-child(odd) th {[m
[31m-  background-color: #393939;[m
[31m-}[m
[31m-.table-dark tbody tr td,[m
[31m-.table-dark tbody tr th,[m
[31m-.table-dark tbody tr:hover td,[m
[31m-.table-dark tbody tr:hover th {[m
[31m-  background-color: #333;[m
[31m-}[m
[31m-[m
[31m-/* STATS THEME */[m
[31m-[m
[31m-.table-stats {[m
[31m-  border:1px solid #C2C2C2;[m
[31m-  border-collapse: separate;[m
[31m-  *border-collapse: collapsed;[m
[31m-  -webkit-border-radius: 0;[m
[31m-  -moz-border-radius: 0;[m
[31m-  border-radius: 0 !important;[m
[31m-  font-family:verdana,helvetica,arial,sans-serif;[m
[31m-  font-size:11px;[m
[31m-  color:#333;[m
[31m-}[m
[31m-.table-stats caption {[m
[31m-  border-left:1px solid #C2C2C2;[m
[31m-  border-right:1px solid #C2C2C2;[m
[31m-  border-top:1px solid #C2C2C2;[m
[31m-  background:#F5F5F5;[m
[31m-  line-height:1.3em;[m
[31m-  background-image: linear-gradient(bottom, #FFF 0%, #E9E9E9 100%);[m
[31m-  background-image: -o-linear-gradient(bottom, #FFF 0%, #E9E9E9 100%);[m
[31m-  background-image: -moz-linear-gradient(bottom, #FFF 0%, #E9E9E9 100%);[m
[31m-  background-image: -webkit-linear-gradient(bottom, #FFF 0%, #E9E9E9 100%);[m
[31m-  background-image: -ms-linear-gradient(bottom, #FFF 0%, #E9E9E9 100%);[m
[31m-[m
[31m-  background-image: -webkit-gradient([m
[31m-  	linear,[m
[31m-  	left bottom,[m
[31m-  	left top,[m
[31m-  	color-stop(0, #FFF),[m
[31m-  	color-stop(1, #E9E9E9)[m
[31m-  );[m
[31m-  padding:10px;[m
[31m-  font-family:helvetica,arial,sans-serif;[m
[31m-  font-size:13px;[m
[31m-  text-shadow:0 1px 0 #FFF;[m
[31m-}[m
[31m-.table-stats.table-bordered {[m
[31m-  border-left: 0;[m
[31m-}[m
[31m-.table-stats th,[m
[31m-.table-stats td {[m
[31m-  background:#FFF;[m
[31m-  color:#666;[m
[31m-  border-top: none;[m
[31m-  border-radius:0 !important;[m
[31m-}[m
[31m-.table-stats thead tr th, .table-stats thead tr.colhead:nth-child(1) th {[m
[31m-  font-size:13px;[m
[31m-  font-weight:bold;[m
[31m-  font-family:helvetica,arial,sans-serif;[m
[31m-  background:#DDD;[m
[31m-  background-image: linear-gradient(bottom, #E8E8E8 0%, #CECECE 100%);[m
[31m-  background-image: -o-linear-gradient(bottom, #E8E8E8 0%, #CECECE 100%);[m
[31m-  background-image: -moz-linear-gradient(bottom, #E8E8E8 0%, #CECECE 100%);[m
[31m-  background-image: -webkit-linear-gradient(bottom, #E8E8E8 0%, #CECECE 100%);[m
[31m-  background-image: -ms-linear-gradient(bottom, #E8E8E8 0%, #CECECE 100%);[m
[31m-[m
[31m-  background-image: -webkit-gradient([m
[31m-  	linear,[m
[31m-  	left bottom,[m
[31m-  	left top,[m
[31m-  	color-stop(0, #E8E8E8),[m
[31m-  	color-stop(1, #CECECE)[m
[31m-  );[m
[31m-  color:#666;[m
[31m-  border-radius:0 !important;[m
[31m-  padding:4px !important;[m
[31m-  border-bottom:none;[m
[31m-}[m
[31m-.table-stats thead tr:nth-child(1) th {[m
[31m-  font-size:13px;[m
[31m-  font-weight:bold;[m
[31m-  font-family:helvetica,arial,sans-serif;[m
[31m-  background:#4B4B4B;[m
[31m-  background-image: linear-gradient(bottom, #565656 0%, #434343 100%);[m
[31m-  background-image: -o-linear-gradient(bottom, #565656 0%, #434343 100%);[m
[31m-  background-image: -moz-linear-gradient(bottom, #565656 0%, #434343 100%);[m
[31m-  background-image: -webkit-linear-gradient(bottom, #565656 0%, #434343 100%);[m
[31m-  background-image: -ms-linear-gradient(bottom, #565656 0%, #434343 100%);[m
[31m-[m
[31m-  background-image: -webkit-gradient([m
[31m-  	linear,[m
[31m-  	left bottom,[m
[31m-  	left top,[m
[31m-  	color-stop(0, #565656),[m
[31m-  	color-stop(1, #434343)[m
[31m-  );[m
[31m-  color:#FFF;[m
[31m-  border-bottom:1px solid #FFF;[m
[31m-  border-radius:0 !important;[m
[31m-}[m
[31m-.table-stats th.headerSortable:hover {[m
[31m-  cursor:pointer;[m
[31m-}[m
[31m-.table-stats th.headerSortDown { background-color:#CCC; }[m
[31m-.table-stats th.headerSortUp { background-color:#CCC; }[m
[31m-.table-stats thead tr:nth-child(1) th.headerSortDown {[m
[31m-  background-color:#333;[m
[31m-  background-image: url('../img/asc_light.gif');[m
[31m-  background-repeat: no-repeat;[m
[31m-  background-position: center right;[m
[31m-}[m
[31m-.table-stats thead tr:nth-child(1) th.headerSortUp {[m
[31m-  background-color:#333;[m
[31m-  background-image: url('../img/desc_light.gif');[m
[31m-  background-repeat: no-repeat;[m
[31m-  background-position: center right;[m
[31m-}[m
[31m-.table-stats.table-bordered th, .table-stats.table-bordered td {[m
[31m-  border-top: 1px solid #C2C2C2;[m
[31m-  border-left: 1px solid #C2C2C2;[m
[31m-}[m
[31m-.table-stats.table-condensed th, .table-stats.table-condensed td {[m
[31m-  padding:1px 4px;[m
[31m-}[m
[31m-.table-stats.table-striped tbody tr:nth-child(even) td,[m
[31m-.table-stats.table-striped tbody tr:nth-child(even) th,[m
[31m-.table-stats.table-striped tbody tr:nth-child(even):hover td,[m
[31m-.table-stats.table-striped tbody tr:nth-child(even):hover th {[m
[31m-  background-color: #F1F1F1;[m
[31m-}[m
[31m-.table-stats.table-striped tbody tr:nth-child(odd) td,[m
[31m-.table-stats.table-striped tbody tr:nth-child(odd) th,[m
[31m-.table-stats.table-striped tbody tr:nth-child(odd):hover td,[m
[31m-.table-stats.table-striped tbody tr:nth-child(odd):hover th {[m
[31m-  background-color: #FFF;[m
[31m-}[m
[31m-.table-stats thead:first-child tr:first-child th,[m
[31m-.table-stats tbody:first-child tr:first-child th,[m
[31m-.table-stats tbody:first-child tr:first-child td {[m
[31m-  border-top: 0;[m
[31m-}[m
[31m-[m
[31m-/* PAPER THEME */[m
[31m-[m
[31m-.table-paper {[m
[31m-  border:1px solid #D0D7E9;[m
[31m-  border-collapse: separate;[m
[31m-  *border-collapse: collapsed;[m
[31m-  -webkit-border-radius: 0;[m
[31m-  -moz-border-radius: 0;[m
[31m-  border-radius: 0 !important;[m
[31m-  font-family:helvetica,arial,sans-serif;[m
[31m-  color:#333;[m
[31m-  box-shadow:0 1px 2px #E5E5E5;[m
[31m-}[m
[31m-.table-paper caption {[m
[31m-  [m
[31m-}[m
[31m-.table-paper.table-bordered {[m
[31m-  border-left: 0;[m
[31m-}[m
[31m-.table-paper thead tr th {[m
[31m-  font-size:13px;[m
[31m-  font-weight:bold;[m
[31m-  background:#EFEFEF;[m
[31m-  color:#666;[m
[31m-  border-radius:0 !important;[m
[31m-  border-top:none;[m
[31m-}[m
[31m-.table-paper th,[m
[31m-.table-paper td {[m
[31m-  background:#FFF;[m
[31m-  color:#666;[m
[31m-  box-shadow:inset 0 1px 0 #D0D7E9;[m
[31m-  border-top:none;[m
[31m-  border-radius:0 !important;[m
[31m-}[m
[31m-.table-paper th.headerSortable:hover {[m
[31m-  cursor:pointer;[m
[31m-}[m
[31m-.table-paper th.headerSortDown { background-color:#D9D9D9; }[m
[31m-.table-paper th.headerSortUp { background-color:#D9D9D9; }[m
[31m-.table-paper.table-bordered th, .table-paper.table-bordered td {[m
[31m-  box-shadow:inset 0 1px 0 #D0D7E9, inset 1px 0 0 #D0D7E9;[m
[31m-  border-left:none;[m
[31m-  border-top:none;[m
[31m-}[m
[31m-.table-paper.table-bordered tbody td:nth-child(2) {[m
[31m-  box-shadow:inset 0 1px 0 #D0D7E9;[m
[31m-  border-left:none;[m
[31m-  border-top:none;[m
[31m-}[m
[31m-.table-paper.table-striped tbody tr:nth-child(even) td,[m
[31m-.table-paper.table-striped tbody tr:nth-child(even) th,[m
[31m-.table-paper.table-striped tbody tr:nth-child(even):hover td,[m
[31m-.table-paper.table-striped tbody tr:nth-child(even):hover th {[m
[31m-  background-color: #F4F6F9;[m
[31m-}[m
[31m-.table-paper.table-striped tbody tr:nth-child(odd) td,[m
[31m-.table-paper.table-striped tbody tr:nth-child(odd) th,[m
[31m-.table-paper.table-striped tbody tr:nth-child(odd):hover td,[m
[31m-.table-paper.table-striped tbody tr:nth-child(odd):hover th {[m
[31m-  background-color: #FFF;[m
[31m-}[m
[31m-.table-paper thead:first-child tr:first-child th,[m
[31m-.table-paper tbody:first-child tr:first-child th,[m
[31m-.table-paper tbody:first-child tr:first-child td {[m
[31m-  box-shadow:none !important;[m
[31m-  border-top:none !important;[m
[31m-}[m
[31m-.table-paper tbody tr th:first-child,[m
[31m-.table-paper tbody tr td:first-child {[m
[31m-  border-right:4px double #EE3531;[m
[31m-  padding-left:10px;[m
[31m-}[m
\ No newline at end of file[m
[1mdiff --git a/templates/base.html b/templates/base.html[m
[1mindex e60fbe9..e8a5873 100644[m
[1m--- a/templates/base.html[m
[1m+++ b/templates/base.html[m
[36m@@ -19,11 +19,8 @@[m
               [m
             </div>[m
         </div>[m
[31m-        {% block outside_content %}{% endblock %}[m
 [m
[31m-  <div class="col-sm-9 col-sm-offset-3 col-md-8 col-md-offset-2 main">[m
         {% block content %}{% endblock %}[m
[31m-        </div>[m
 [m
         <script type="text/javascript" src="{% static 'js/jquery-1.11.0.min.js' %}"></script> [m
         <script type="text/javascript" src="{% static 'js/bootstrap.min.js' %}"></script>[m
[1mdiff --git a/templates/profiles/edit_profile.html b/templates/profiles/edit_profile.html[m
[1mindex 836d4e9..c5ad45e 100644[m
[1m--- a/templates/profiles/edit_profile.html[m
[1m+++ b/templates/profiles/edit_profile.html[m
[36m@@ -5,7 +5,8 @@[m
 {% block content %}[m
 <h1>Edit contact info for {{ user.username }}</h1>[m
 <form action="" method="POST">{% csrf_token %}[m
[31m-{{ form.as_p}}[m
[31m-<input id="submit" type="submit" name="submit" value="Update" />[m
[31m-</form>[m
[32m+[m[32m{{ form }}[m
[32m+[m[32m<input id="submit" type="submit" name="submit" value="Update" /></form>[m
[32m+[m
[32m+[m[41m [m
 {% endblock content %}[m
[1mdiff --git a/templates/profiles/profile_base.html b/templates/profiles/profile_base.html[m
[1mindex cfc029d..2215444 100644[m
[1m--- a/templates/profiles/profile_base.html[m
[1m+++ b/templates/profiles/profile_base.html[m
[36m@@ -4,11 +4,12 @@[m
 [m
 [m
 {% block navbar-right %}[m
[32m+[m[32m  {% if auth_user  %}[m
     <ul class="nav navbar-nav navbar-right">[m
         <li class="dropdown">[m
[31m-            <a id="drop1" href="#" role="button" class="dropdown-toggle" data-toggle="dropdown">{{ user.first_name }}<b class="caret"></b></a>[m
[32m+[m[32m            <a id="drop1" href="#" role="button" class="dropdown-toggle" data-toggle="dropdown">{{ auth_user.first_name }}<b class="caret"></b></a>[m
             <ul class="dropdown-menu" role="menu" aria-labelledby="drop1">[m
[31m-                <li role="presentation"><a role="menuitem" tabindex="-1" href="{% url 'profiles_profile_detail' username=user.username %} ">Profile</a></li>[m
[32m+[m[32m                <li role="presentation"><a role="menuitem" tabindex="-1" href="{% url 'profiles_profile_detail' username=auth_user.username %} ">Profile</a></li>[m
                 <li role="presentation"><a role="menuitem" tabindex="-1" href="{% url 'edit_account' %}">Account Info</a></li>[m
                 <li role="presentation"><a role="menuitem" tabindex="-1" href="#"><span class="text-muted">Settings</span></a></li>[m
                 <li role="presentation" class="divider"></li>[m
[36m@@ -17,20 +18,21 @@[m
                 <li role="presentation"><a role="menuitem" tabindex="-1" href="{% url 'auth_logout' %}">Logout</a></li>[m
             </ul>[m
         </li>[m
[31m-        <li style="margin-right: 50px"></li>[m
     </ul>[m
[32m+[m[32m  {% endif %}[m
 {% endblock navbar-right %}[m
 [m
 [m
 [m
   {% block content %}[m
 [m
[31m-[m
[32m+[m[32m  <div class="col-sm-9 col-sm-offset-3 col-md-8 col-md-offset-2 main">[m
[32m+[m[32m    {% if auth_user  == profile.user %}[m
     <h1 class="page-header">Dashboard</h1>[m
     <div class="row placeholders">[m
           <div class="col-md-4">[m
           {% block nav_item_1 %}[m
[31m-            <a href="#"><img alt="120x120" src="{% static 'img/icon/myshedsicon140.png' %}" style="width: 100px; height: 100px;">[m
[32m+[m[32m            <a href="#"><img alt="140x140" src="{% static 'img/icon/myshedsicon140.png' %}" style="width: 140px; height: 140px;">[m
             <h4>My Sheds</h4></a>[m
             <span class="text-muted">Manage your sheds</span>[m
           {% endblock %}[m
[36m@@ -38,7 +40,7 @@[m
 [m
           <div class="col-md-4">[m
           {% block nav_item_2 %}[m
[31m-            <a href="#"><img alt="120x120" src="{% static 'img/icon/mysharezoneicon140.png' %}" style="width: 100px; height: 100px;">[m
[32m+[m[32m            <a href="#"><img alt="140x140" src="{% static 'img/icon/mysharezoneicon140.png' %}" style="width: 140px; height: 140px;">[m
             <h4>Share Zone</h4></a>[m
             <span class="text-muted">Find and borrow tools</span>[m
             {% endblock %}[m
[36m@@ -46,12 +48,16 @@[m
 [m
           <div class="col-md-4">[m
           {% block nav_item_3 %}[m
[31m-            <a href="#"><img alt="120x120" src="{% static 'img/icon/mytoolsicon140.png' %}" style="width: 100px; height: 100px;">[m
[32m+[m[32m            <a href="#"><img alt="140x140" src="{% static 'img/icon/mytoolsicon140.png' %}" style="width: 140px; height: 140px;">[m
             <h4>My Tools</h4></a>[m
             <span class="text-muted">Manage your tools</span>[m
             {% endblock %}[m
         </div>[m
     </div>[m
[32m+[m[32m    {% endif %}[m
[32m+[m[32m    {% block inner_content %}{% endblock %}[m
[32m+[m[32m    </div>[m
 [m
   {% endblock content %}[m
 [m
[41m+[m
[1mdiff --git a/templates/profiles/profile_detail.html b/templates/profiles/profile_detail.html[m
[1mindex 963599c..650c8e6 100644[m
[1m--- a/templates/profiles/profile_detail.html[m
[1m+++ b/templates/profiles/profile_detail.html[m
[36m@@ -2,10 +2,7 @@[m
 {% load staticfiles %}[m
 {% block title %}Profile - {{ profile.user.username }}{% endblock %} [m
 [m
[31m-{% block content %} [m
[31m-    {% if user == profile.user %}[m
[31m-        {{ block.super }}[m
[31m-    {% endif %}[m
[32m+[m[32m{% block inner_content %}[m[41m [m
     <h1 class="page-header">Profile <small>{{ profile.user.username }}</small></h1>[m
         <div class="row">[m
             <div class="col-md-6 text-right">[m
[36m@@ -39,5 +36,4 @@[m
               </table>[m
             </div>[m
           </div>[m
[31m-[m
 {% endblock %}[m
\ No newline at end of file[m
[1mdiff --git a/templates/registration/login.html b/templates/registration/login.html[m
[1mindex e0e9e5c..21d0d20 100644[m
[1m--- a/templates/registration/login.html[m
[1m+++ b/templates/registration/login.html[m
[36m@@ -5,8 +5,9 @@[m
 {% block css%}[m
 <link href="{% static 'css/login.css' %}" rel="stylesheet" type="text/css">[m
 {% endblock %}[m
[31m-{% block outside_content %}[m
[31m-[m
[32m+[m[32m{% block content %}[m
[32m+[m[32m{% url 'auth_password_reset' as auth_pwd_reset_url %}[m
[32m+[m[32m{% url 'registration_register' as register_url%}[m
 [m
 {% if form.errors %}[m
 <p>{% blocktrans %}Your username and password didn't match. Please try again.{% endblocktrans %}</p>[m
[36m@@ -19,14 +20,27 @@[m
             <input id="id_username"  class="form-control" placeholder="Username" maxlength="254" name="username" type="text" required autofocus>[m
             <input id="id_password"  class="form-control" placeholder="Password" maxlength="254" name="password" type="password" required>[m
         </p>[m
[32m+[m[32m    <!--[m
[32m+[m[32m    <table>[m
[32m+[m[32m    <tr>[m
[32m+[m[32m        <td>{% trans form.username.label_tag %}</td>[m
[32m+[m[32m        <td>{{ form.username }}</td>[m
[32m+[m[32m    </tr>[m
[32m+[m[32m    <tr>[m
[32m+[m[32m        <td>{% trans form.password.label_tag %}</td>[m
[32m+[m[32m        <td>{{ form.password }}</td>[m
[32m+[m[32m    </tr>[m
[32m+[m[32m    </table> -->[m
[32m+[m[32m    <!-- <p>{% blocktrans %}<a href="{{ auth_pwd_reset_url }}">Forgot</a> your password?[m
[32m+[m[32m        <a href="{{ register_url }}">Need an account</a>?{% endblocktrans %}</p>-->[m
 [m
         <input type="submit" class="btn btn-lg btn-primary btn-block" value="{% trans "Log In" %}" />[m
         <input type="hidden" name="next" value="{{ next }}" />[m
         <p>[m
             <hr>[m
[31m-            <span class="text-muted">New here? <a href="{% url 'registration_register' %}" class="text-muted"><b>Create an account.</b></a></span>[m
[32m+[m[32m            {% blocktrans %}<span class="text-muted">New here? <a href="{{ register_url }}" class="text-muted"><b>Create an account.</b></a></span>{% endblocktrans %}[m
             <br>[m
[31m-          <!--  <a href="{% url 'auth_password_reset' %}" class="text-muted">Forgot your password?</a> -->[m
[32m+[m[32m            <a href="{{ auth_pwd_reset_url }}" class="text-muted">Forgot your password?</a>[m
         </p>[m
     </form>[m
 </div>[m
[1mdiff --git a/templates/registration/registration_form.html b/templates/registration/registration_form.html[m
[1mindex 69cdd9f..4322884 100644[m
[1m--- a/templates/registration/registration_form.html[m
[1m+++ b/templates/registration/registration_form.html[m
[36m@@ -10,15 +10,14 @@[m
     }[m
 </style>[m
 {% endblock %}[m
[31m-{% block outside_content %}[m
[32m+[m[32m{% block content %}[m
 <div class="container">[m
 <div class="col-sm-4 col-sm-offset-4 text-center">[m
     <h2>Sign Up</h2>[m
     <hr>[m
     <form  method='post' action='' role="form">{% csrf_token %}[m
 [m
[31m-    {% if form.errors %}[m
[31m-        {% for field, errors in form.errors.items %}[m
[32m+[m[32m                {% for field, errors in form.errors.items %}[m
             <ul class="errorlist">[m
             {% for error in errors %}[m
                 <li>{{ error }}</li>[m
[36m@@ -26,7 +25,6 @@[m
             {% endfor %}[m
             </ul>[m
         {% endfor %}[m
[31m-        {% endif %}[m
 [m
         <div class="form-inline form-group">[m
                 <input id="id_first_name" class="form-control input-inline" maxlength="30" name="first_name" placeholder="First Name" type="text">[m
[1mdiff --git a/templates/tools/create_tool.html b/templates/tools/create_tool.html[m
[1mdeleted file mode 100644[m
[1mindex 0a702d6..0000000[m
[1m--- a/templates/tools/create_tool.html[m
[1m+++ /dev/null[m
[36m@@ -1,32 +0,0 @@[m
[31m-[m
[31m-{% extends "tools/tool_base.html" %}[m
[31m-{% load staticfiles %}[m
[31m-{% block title %}Create Tool{% endblock %}[m
[31m- [m
[31m-{% block content %}[m
[31m-	{{block.super}}[m
[31m-	<h1 class="page-header">Create a Tool</h1>[m
[31m-	[m
[31m-		<div class="row">[m
[31m-		<div class="col-md-6 text-right">[m
[31m-			<img class="img-circle" alt="image of tool" src="{% static 'img/icon/profileicon140.png' %}" style="width: 200px; height:200px;">[m
[31m-		</div>[m
[31m-	[m
[31m-	<form method='post' action='' role="form">{% csrf_token %}[m
[31m-	[m
[31m-	{% for field, errors in form.errors.items %}[m
[31m-            <ul class="errorlist">[m
[31m-            {% for error in errors %}[m
[31m-                <li>{{ error }}</li>[m
[31m-                [m
[31m-            {% endfor %}[m
[31m-            </ul>[m
[31m-        {% endfor %}[m
[31m-	[m
[31m-		<div class="col-md-6 text-left">[m
[31m-			{{Forms}}[m
[31m-			<hr>[m
[31m-			<input class="btn btn-lg btn-primary btn-block" type="submit" value="{% trans "Create Tool" %}"/>[m
[31m-		</div>[m
[31m-	</form>[m
[31m-{% endblock %}[m
[1mdiff --git a/templates/tools/tool_base.html b/templates/tools/tool_base.html[m
[1mdeleted file mode 100644[m
[1mindex 704103d..0000000[m
[1m--- a/templates/tools/tool_base.html[m
[1m+++ /dev/null[m
[36m@@ -1,6 +0,0 @@[m
[31m-{% extends "profiles/profile_base.html" %}[m
[31m-{% load staticfiles %}[m
[31m-{% load i18n %}[m
[31m-[m
[31m-[m
[31m-[m
[1mdiff --git a/templates/tools/tool_detail.html b/templates/tools/tool_detail.html[m
[1mdeleted file mode 100644[m
[1mindex b796444..0000000[m
[1m--- a/templates/tools/tool_detail.html[m
[1m+++ /dev/null[m
[36m@@ -1,44 +0,0 @@[m
[31m-{% extends "tools/tool_base.html" %}[m
[31m-{% load staticfiles %}[m
[31m-{% block title %}Tool - {{ tool.name }}{% endblock %} [m
[31m-[m
[31m-{% block content %} [m
[31m-{{block.super}}[m
[31m-    <h1 class="page-header">Tool <small>{{ tool.name }}</small></h1>[m
[31m-        <div class="row">[m
[31m-            <div class="col-md-6 text-right">[m
[31m-                <img class="img-circle" alt="170x170" src="{% static 'img/icon/profileicon140.png' %}" style="width: 200px; height: 200px;">[m
[31m-            </div>[m
[31m-         [m
[31m-            <div class="col-md-6 text-left">[m
[31m-              <table class="table no-border detail-table">[m
[31m-                <tbody>[m
[31m-                  <tr>[m
[31m-                    <td class="text-muted label-col">Name: </td>[m
[31m-                    <td>{{ tool.name }}</td>[m
[31m-                  </tr>[m
[31m-                  <tr>[m
[31m-                    <td class="text-muted">Shed: </td>[m
[31m-                    <td>{{ tool.Shed }}</td>[m
[31m-                  </tr>[m
[31m-                  <tr>[m
[31m-                    <td class="text-muted">Owner </td>[m
[31m-                    <td>{{ tool.owner.name }}</td>[m
[31m-                  </tr>[m
[31m-                  <tr>[m
[31m-                    <td class="text-muted">Borrower </td>[m
[31m-                    <td>{{ tool.borrower.name }}</td>[m
[31m-                  </tr>[m
[31m-                  <tr>[m
[31m-                    <td class="text-muted">Category </td>[m
[31m-                    <td>{{ tool.category }}</td>[m
[31m-                  </tr>[m
[31m-				  <tr>[m
[31m-                    <td class="text-muted">Description  </td>[m
[31m-                    <td>{{ tool.description }}</td>[m
[31m-                  </tr>[m
[31m-                </tbody>[m
[31m-              </table>[m
[31m-            </div>[m
[31m-          </div>[m
[31m-{% endblock %}[m
\ No newline at end of file[m
[1mdiff --git a/templates/users/edit_account.html b/templates/users/edit_account.html[m
[1mindex ae12d9d..7584fc8 100644[m
[1m--- a/templates/users/edit_account.html[m
[1m+++ b/templates/users/edit_account.html[m
[36m@@ -1,24 +1,12 @@[m
 [m
[31m-{% extends "profiles/profile_base.html" %}[m
[31m-{% block title %}Edit Account - {{ user.username }} {% endblock %}[m
[31m-[m
[32m+[m[32m{% extends "base.html" %}[m
[32m+[m[32m{% block title %}Edit Profile -  {{ user.username }} {% endblock %}[m
[32m+[m[41m [m
 {% block content %}[m
[31m-{{ block.super }}[m
[31m-<h1 class="page-header">Edit Account</h1>[m
[31m-    <div class="col-sm-4 col-sm-offset-4">[m
[31m-    {% if form.errors %}[m
[31m-        {% for field, errors in form.errors.items %}[m
[31m-            <ul class="errorlist">[m
[31m-            {% for error in errors %}[m
[31m-                <li>{{ error }}</li>         [m
[31m-            {% endfor %}[m
[31m-            </ul>[m
[31m-        {% endfor %}[m
[31m-    {% endif %}[m
[31m-    <form action="" method='POST' role='form'>{% csrf_token %}[m
[31m-        {{form.as_p}}[m
[31m-        <input id="submit" type="submit" name="submit" value="Update" />[m
[31m-    </form>[m
[31m- </div>[m
[31m-[m
[31m-{% endblock %}[m
[32m+[m[32m<h1>Edit contact info for {{ user.username }}</h1>[m
[32m+[m[32m<form action="" method="POST">{% csrf_token %}[m
[32m+[m[32m{{ form }}[m
[32m+[m[32m<input id="submit" type="submit" name="submit" value="Update" /></form>[m
[32m+[m[32m</form>[m
[32m+[m[41m [m
[32m+[m[32m{% endblock content %}[m
[1mdiff --git a/toolshare/urls.py b/toolshare/urls.py[m
[1mindex e05a1f1..7215272 100644[m
[1m--- a/toolshare/urls.py[m
[1m+++ b/toolshare/urls.py[m
[36m@@ -2,13 +2,13 @@[m [mfrom django.conf.urls import patterns, include, url[m
 from django.views.generic import RedirectView[m
 from django.contrib import admin[m
 admin.autodiscover()[m
[31m-from users.forms import CustomRegistrationForm, ProfileForm, CustomPasswordChangeForm[m
[32m+[m[32mfrom users.forms import CustomRegistrationForm, ProfileForm[m
 [m
 from registration.backends.default.views import RegistrationView[m
 from profiles import views as ProfileView[m
 from users import views as UserView[m
 [m
[31m-from django.views.generic import TemplateView[m
[32m+[m
 urlpatterns = patterns('',[m
     # Examples:[m
     # url(r'^$', 'toolshare.views.home', name='home'),[m
[36m@@ -18,16 +18,10 @@[m [murlpatterns = patterns('',[m
     url(r'^register/$', [m
        RegistrationView.as_view(form_class = CustomRegistrationForm), [m
        name = 'registration_register'),[m
[31m-    url(r'^account/edit', 'django.contrib.auth.views.password_change', {'template_name': 'users/edit_account.html', [m
[31m-          'password_change_form':CustomPasswordChangeForm, 'extra_context': {'auth_user':'request.user'}}, name='edit_account'),[m
[31m-    #url(r'^account/edit/', UserView.edit_account, name='edit_account'),[m
[32m+[m[32m    url(r'^edit/', UserView.edit_account, name='edit_account'),[m
     #url(r'^profile/edit', 'profiles.views.edit_profile', {'form_class': ProfileForm,}),[m
     url(r'^', include('registration.backends.default.urls')),[m
     url(r'^profile/$', UserView.user_home, name='user_home' ),[m
     url(r'^profile/', include('profiles.urls')),[m
[31m-    url(r'^account/password_changed', TemplateView.as_view(template_name='registration/password_change_done.html'), [m
[31m-                                                                                                                                          name='password_change_done'),[m
[31m-    url(r'^tool_detail', TemplateView.as_view(template_name='tools/tool_detail.html'), [m
[31m-                                                                                                                                          name='tool_detail'),[m
 [m
 )[m
[1mdiff --git a/users/forms.py b/users/forms.py[m
[1mindex a17e34c..087a4e5 100644[m
[1m--- a/users/forms.py[m
[1m+++ b/users/forms.py[m
[36m@@ -18,37 +18,14 @@[m [mfrom django.contrib.auth.models import User[m
 [m
 [m
  [m
[31m-class AccountForm(forms.Form):[m
[32m+[m[32mclass AccountForm(ModelForm):[m
     """[m
     Form for editting account info.[m
     """[m
[31m-    first_name = forms.CharField(label='First Name', max_length=30)[m
[31m-    last_name = forms.CharField(label='Last Name', max_length=30)[m
[31m-    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)[m
[31m-    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)[m
[31m-    email = forms.EmailField(label='E-Mail')[m
 [m
[31m-    def clean_password(self):[m
[31m-        """[m
[31m-        Verifiy that the values entered into the two password fields[m
[31m-        match. Note that an error here will end up in[m
[31m-        ``non_field_errors()`` because it doesn't apply to a single[m
[31m-        field.[m
[31m-        """[m
[31m-        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:[m
[31m-            if self.cleaned_data['password1'] != self.cleaned_data['password2']:[m
[31m-                raise forms.ValidationError("The two password fields didn't match.")[m
[31m-        return self.cleaned_data[m
[31m-[m
[31m-    def clean_email(self):[m
[31m-        """[m
[31m-        Validate that the supplied email address is unique for the[m
[31m-        site.[m
[31m-        [m
[31m-        """[m
[31m-        if User.objects.filter(email__iexact=self.cleaned_data['email']):[m
[31m-            raise forms.ValidationError("This email address is already in use. ")[m
[31m-        return self.cleaned_data['email'][m
[32m+[m[32m    class Meta:[m
[32m+[m[32m        model = User[m
[32m+[m[32m        exclude = ('last_login', 'date_joined', 'is_active', 'is_superuser', 'user_permissions', 'groups', 'is_staff')[m
 [m
  [m
 class ProfileForm(ModelForm):[m
[36m@@ -60,9 +37,3 @@[m [mclass ProfileForm(ModelForm):[m
     class Meta:[m
         model = UserProfile[m
         #exclude = ('field1','field2','field3',)[m
[31m-[m
[31m-from django.contrib.auth.forms import PasswordChangeForm[m
[31m-class CustomPasswordChangeForm(PasswordChangeForm):[m
[31m-    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))[m
[31m-    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))[m
[31m-    new_password2 = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))[m
\ No newline at end of file[m
[1mdiff --git a/users/models.py b/users/models.py[m
[1mindex efb8a53..d54a184 100644[m
[1m--- a/users/models.py[m
[1m+++ b/users/models.py[m
[36m@@ -6,7 +6,7 @@[m [mclass UserProfile(models.Model):[m
     Each User has a UserProfile associated with it. UserProfile holds extra information [m
     about the user.[m
     """[m
[31m-    user = models.OneToOneField(User, related_name='profile') # Each User can have only 1 UserProfile[m
[32m+[m[32m    user = models.OneToOneField(User) # Each User can have only 1 UserProfile[m
     postal_code = models.CharField(verbose_name='postal code', max_length=10)[m
 [m
 [m
[1mdiff --git a/users/views.py b/users/views.py[m
[1mindex 55816d6..2e9a651 100644[m
[1m--- a/users/views.py[m
[1m+++ b/users/views.py[m
[36m@@ -4,7 +4,6 @@[m [mfrom django.shortcuts import render_to_response[m
 from django.template import RequestContext[m
 from django.core.urlresolvers import reverse[m
 from django.contrib.auth.decorators import login_required[m
[31m-from django import forms[m
 from profiles import  views as ProfileView[m
 from users.forms import AccountForm[m
 [m
[36m@@ -14,3 +13,24 @@[m [mdef user_home(request):[m
     else:[m
         return redirect(reverse('auth_login'))[m
 [m
[32m+[m
[32m+[m[32mdef edit_account(request, template_name='users/edit_account.html'):[m
[32m+[m[32m    context = RequestContext(request)[m
[32m+[m[32m    if request.method == 'POST':[m
[32m+[m[32m        form = AccountForm(data=request.POST)[m
[32m+[m[32m        if form.is_valid():[m
[32m+[m[32m            form.save()[m
[32m+[m[32m            return redirect(request.path)[m
[32m+[m[32m    else:[m
[32m+[m[32m        form = AccountForm(instance=request.user)[m
[32m+[m[32m    return render_to_response(template_name, {'form': form, 'user': request.user},[m[41m [m
[32m+[m[32m                                                                    context_instance=context)[m
[32m+[m
[32m+[m[32m# Currently unused[m
[32m+[m[32mdef login_check(request, next=None):[m
[32m+[m[32m    if request.user.is_authenticated():[m
[32m+[m[32m        return redirect(reverse(next))[m
[32m+[m[32m    else:[m
[32m+[m[32m        return redirect(reverse('auth_login'))[m
[41m+[m
[41m+[m
