
import borrow_requests.RequestStatus as rs
def borrow_request_status(request):
    """
    Returns tuple of request status definitions.
    """
    status_dict = { 'APPROVED': rs.APPROVED, 'DENIED': rs.DENIED, 
                                            'PENDING': rs.PENDING, 'CANCELED': rs.CANCELED }
    return {'br_status':  status_dict, }
