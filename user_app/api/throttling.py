from rest_framework.throttling import UserRateThrottle


class ReviewCreateThrottling(UserRateThrottle):
    scope = 'review-create'


class ReviewListThrottling(UserRateThrottle):
    scope = 'review-list'
