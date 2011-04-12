from django.core.exceptions import ObjectDoesNotExist

from features.models import Feature, FeatureSet, SiteFeatureArea
from articles.models import Article

def get_features(area):
    # Get the right feature_set
    try:
        site_feature_area = SiteFeatureArea.site_objects.get(area=area)
        feature_set = FeatureSet.objects.get(site_feature_area=site_feature_area)
    except ObjectDoesNotExist:
        """
        We don't have a corresponding feature_area, or a
        feature_set, so we don't return any features
        """
        return [] # return nothing
    else:
        """
        With the right feature_set, try to build a list of features
        """
        feature_filter_kwargs = {
            'active': True,
            'feature_set': feature_set,}
        features = Feature.objects.filter(**feature_filter_kwargs).order_by("order")
        return features
