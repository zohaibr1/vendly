from django.utils import timezone

def approve_refund(refund, user):
    refund.status="approved"
    refund.processed_by=user
    refund.processed_at=timezone.now()
    refund.save()
    return refund

def reject_refund(refund,user, reason=None):
    refund.status="rejected"
    refund.processed_by=user
    refund.processed_at=timezone.now()
    if reason:
        refund.reason=reason
    refund.save()
    return refund
