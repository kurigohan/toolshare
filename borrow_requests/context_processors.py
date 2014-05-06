from borrow_requests.models import BorrowRequest
import borrow_requests.RequestStatus as rs

def borrow_request_status(request):
    """
    Returns tuple of request status definitions.
    """
    if request.user.is_authenticated():
        status_dict = { 'APPROVED': rs.APPROVED, 'DENIED': rs.DENIED, 
                                                'PENDING': rs.PENDING, 'CANCELED': rs.CANCELED }
        return {'br_status':  status_dict, }
    else:
        return{}

def borrow_request_new(request):
    """
    Indicates if there are new borrow requests
    """
    if request.user.is_authenticated():
        has_new = False
        if BorrowRequest.objects.filter(recipient=request.user, status=rs.PENDING) .count() > 0:
            has_new = True
        return {'new_br': has_new}
    else:
        return {}