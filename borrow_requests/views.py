from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from sharecenter.models import Tool, Shed
from notifications.models import Notification
from borrow_requests.models import BorrowRequest
import notifications.NoticeType as NoticeType
import sharecenter.RequestStatus as RequestStatus

@login_required
def approve_borrow_request(request, br_id):
    """
    Approve borrow request
    """
    borrow_request  = get_object_or_404(BorrowRequest, pk=br_id)
    # check if user is recipient of the borrow request
    if borrow_request.recipient == request.user:
        tool = get_object_or_404(Tool, pk=borrow_request.tool.id);
        # check if owner of tool is the recipient of the borrow request
        if tool.owner == request.user and tool.is_available():
            tool.borrow_tool(borrow_request.sender);
            tool.save();
            # notify requester that the request was approved
            Notification.objects.create(recipient=borrow_request.sender, 
                                                        sender=request.user,
                                                        tool=tool,
                                                        notice_type=NoticeType.REQUEST,
                                                        action="approved") 
            borrow_request.update(status=RequestStatus.APPROVED)
            borrow_request.save()
        else:
            messages.error(request, 'Request could not be approved.')  

    return  redirect('view_requests')



@login_required
def deny_borrow_request(request, br_id):
    """
    Deny tool borrow request
    """
    borrow_request  = get_object_or_404(BorrowRequest, pk=br_id)
    # check if user is recipient of the borrow request
    if borrow_request.recipient == request.user:
        tool = get_object_or_404(Tool, pk=borrow_request.tool.id);
        # check if owner of tool is the recipient of the borrow request
        if tool.owner == request.user:
            # notify requester that the request was denied
            Notification.objects.create(recipient=borrow_request.sender, 
                                                        sender=request.user,
                                                        tool=tool,
                                                        notice_type=NoticeType.REQUEST,
                                                        action="denied") 
            borrow_request.update(status=RequestStatus.DENIED)
            borrow_request.save()
        else:
            messages.error(request, 'Request could not be denied.')  
    return  redirect('view_requests')

@login_required
def sender_cancel_request(request, br_id):
    """
    Cancel the borrow request if it is pending.
    """
    borrow_request  = get_object_or_404(BorrowRequest, pk=br_id)
    if borrow_request.sender== request.user and borrow_request.status == RequestStatus.PENDING:
        borrow_request.update(status=RequestStatus.CANCELED)
        borrow_request.save()
        Notification.objects.create(recipient=borrow_request.recipient, 
                                                    sender=request.user,
                                                    tool=borrow_request.tool,
                                                    notice_type=NoticeType.REQUEST,
                                                    action="canceled") 
    else:
        messages.error(request, 'Request cannot be canceled.')
    return redirect('view_requests')

@login_required
def sender_delete_request(request, br_id):
    """
    Set s_deleted to true. The borrow request will no longer appear in the user's 'sent requests' list
    - If s_deleted and r_deleted are both true, then the borrow request will be
    deleted. 
    """
    borrow_request  = get_object_or_404(BorrowRequest, pk=br_id)
    if borrow_request.recipient == request.user:
        if borrow_request.r_deleted:
            borrow_request.delete()
        else:
            borrow_request.update(s_deleted=True)
            borrow_request.save()
    else:
        messages.error(request, 'Request could not be deleted.')  
    return  redirect('view_requests')

@login_required
def recipient_delete_request(request, br_id):
    """
    Set r_deleted to true. The borrow request will no longer appear in the user's 'recieved requests' list
    - If s_deleted and r_deleted are both true, then the borrow request will be
    deleted. 
    """
    borrow_request  = get_object_or_404(BorrowRequest, pk=br_id)
    if borrow_request.recipient == request.user:
        if borrow_request.s_deleted:
            borrow_request.delete()
        else:
            borrow_request.update(r_deleted=True)
            borrow_request.save()
    else:
        messages.error(request, 'Request could not be deleted.')  
    return  redirect('view_requests')