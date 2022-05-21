# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, double, integer


class Alarm(AWSObject):
    """
    `Alarm <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-alarm.html>`__
    """

    resource_type = "AWS::Lightsail::Alarm"

    props: PropsDictType = {
        "AlarmName": (str, True),
        "ComparisonOperator": (str, True),
        "ContactProtocols": ([str], False),
        "DatapointsToAlarm": (integer, False),
        "EvaluationPeriods": (integer, True),
        "MetricName": (str, True),
        "MonitoredResourceName": (str, True),
        "NotificationEnabled": (boolean, False),
        "NotificationTriggers": ([str], False),
        "Threshold": (double, True),
        "TreatMissingData": (str, False),
    }


class AccessRules(AWSProperty):
    """
    `AccessRules <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-bucket-accessrules.html>`__
    """

    props: PropsDictType = {
        "AllowPublicOverrides": (boolean, False),
        "GetObject": (str, False),
    }


class Bucket(AWSObject):
    """
    `Bucket <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-bucket.html>`__
    """

    resource_type = "AWS::Lightsail::Bucket"

    props: PropsDictType = {
        "AccessRules": (AccessRules, False),
        "BucketName": (str, True),
        "BundleId": (str, True),
        "ObjectVersioning": (boolean, False),
        "ReadOnlyAccessAccounts": ([str], False),
        "ResourcesReceivingAccess": ([str], False),
        "Tags": (Tags, False),
    }


class Certificate(AWSObject):
    """
    `Certificate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-certificate.html>`__
    """

    resource_type = "AWS::Lightsail::Certificate"

    props: PropsDictType = {
        "CertificateName": (str, True),
        "DomainName": (str, True),
        "SubjectAlternativeNames": ([str], False),
        "Tags": (Tags, False),
    }


class EnvironmentVariable(AWSProperty):
    """
    `EnvironmentVariable <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-environmentvariable.html>`__
    """

    props: PropsDictType = {
        "Value": (str, False),
        "Variable": (str, False),
    }


class PortInfo(AWSProperty):
    """
    `PortInfo <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-portinfo.html>`__
    """

    props: PropsDictType = {
        "Port": (str, False),
        "Protocol": (str, False),
    }


class ContainerProperty(AWSProperty):
    """
    `ContainerProperty <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-container.html>`__
    """

    props: PropsDictType = {
        "Command": ([str], False),
        "ContainerName": (str, False),
        "Environment": ([EnvironmentVariable], False),
        "Image": (str, False),
        "Ports": ([PortInfo], False),
    }


class HealthCheckConfig(AWSProperty):
    """
    `HealthCheckConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-healthcheckconfig.html>`__
    """

    props: PropsDictType = {
        "HealthyThreshold": (integer, False),
        "IntervalSeconds": (integer, False),
        "Path": (str, False),
        "SuccessCodes": (str, False),
        "TimeoutSeconds": (integer, False),
        "UnhealthyThreshold": (integer, False),
    }


class PublicEndpoint(AWSProperty):
    """
    `PublicEndpoint <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-publicendpoint.html>`__
    """

    props: PropsDictType = {
        "ContainerName": (str, False),
        "ContainerPort": (integer, False),
        "HealthCheckConfig": (HealthCheckConfig, False),
    }


class ContainerServiceDeployment(AWSProperty):
    """
    `ContainerServiceDeployment <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-containerservicedeployment.html>`__
    """

    props: PropsDictType = {
        "Containers": ([ContainerProperty], False),
        "PublicEndpoint": (PublicEndpoint, False),
    }


class PublicDomainName(AWSProperty):
    """
    `PublicDomainName <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-container-publicdomainname.html>`__
    """

    props: PropsDictType = {
        "CertificateName": (str, False),
        "DomainNames": ([str], False),
    }


class Container(AWSObject):
    """
    `Container <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-container.html>`__
    """

    resource_type = "AWS::Lightsail::Container"

    props: PropsDictType = {
        "ContainerServiceDeployment": (ContainerServiceDeployment, False),
        "IsDisabled": (boolean, False),
        "Power": (str, True),
        "PublicDomainNames": ([PublicDomainName], False),
        "Scale": (integer, True),
        "ServiceName": (str, True),
        "Tags": (Tags, False),
    }


class RelationalDatabaseParameter(AWSProperty):
    """
    `RelationalDatabaseParameter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-database-relationaldatabaseparameter.html>`__
    """

    props: PropsDictType = {
        "AllowedValues": (str, False),
        "ApplyMethod": (str, False),
        "ApplyType": (str, False),
        "DataType": (str, False),
        "Description": (str, False),
        "IsModifiable": (boolean, False),
        "ParameterName": (str, False),
        "ParameterValue": (str, False),
    }


class Database(AWSObject):
    """
    `Database <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-database.html>`__
    """

    resource_type = "AWS::Lightsail::Database"

    props: PropsDictType = {
        "AvailabilityZone": (str, False),
        "BackupRetention": (boolean, False),
        "CaCertificateIdentifier": (str, False),
        "MasterDatabaseName": (str, True),
        "MasterUserPassword": (str, False),
        "MasterUsername": (str, True),
        "PreferredBackupWindow": (str, False),
        "PreferredMaintenanceWindow": (str, False),
        "PubliclyAccessible": (boolean, False),
        "RelationalDatabaseBlueprintId": (str, True),
        "RelationalDatabaseBundleId": (str, True),
        "RelationalDatabaseName": (str, True),
        "RelationalDatabaseParameters": ([RelationalDatabaseParameter], False),
        "RotateMasterUserPassword": (boolean, False),
        "Tags": (Tags, False),
    }


class AutoSnapshotAddOn(AWSProperty):
    """
    `AutoSnapshotAddOn <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-autosnapshotaddon.html>`__
    """

    props: PropsDictType = {
        "SnapshotTimeOfDay": (str, False),
    }


class AddOn(AWSProperty):
    """
    `AddOn <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-addon.html>`__
    """

    props: PropsDictType = {
        "AddOnType": (str, True),
        "AutoSnapshotAddOnRequest": (AutoSnapshotAddOn, False),
        "Status": (str, False),
    }


class Disk(AWSObject):
    """
    `Disk <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-disk.html>`__
    """

    resource_type = "AWS::Lightsail::Disk"

    props: PropsDictType = {
        "AddOns": ([AddOn], False),
        "AvailabilityZone": (str, False),
        "DiskName": (str, True),
        "SizeInGb": (integer, True),
        "Tags": (Tags, False),
    }


class CacheBehavior(AWSProperty):
    """
    `CacheBehavior <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-cachebehavior.html>`__
    """

    props: PropsDictType = {
        "Behavior": (str, False),
    }


class CacheBehaviorPerPath(AWSProperty):
    """
    `CacheBehaviorPerPath <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-cachebehaviorperpath.html>`__
    """

    props: PropsDictType = {
        "Behavior": (str, False),
        "Path": (str, False),
    }


class CookieObject(AWSProperty):
    """
    `CookieObject <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-cookieobject.html>`__
    """

    props: PropsDictType = {
        "CookiesAllowList": ([str], False),
        "Option": (str, False),
    }


class HeaderObject(AWSProperty):
    """
    `HeaderObject <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-headerobject.html>`__
    """

    props: PropsDictType = {
        "HeadersAllowList": ([str], False),
        "Option": (str, False),
    }


class QueryStringObject(AWSProperty):
    """
    `QueryStringObject <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-querystringobject.html>`__
    """

    props: PropsDictType = {
        "Option": (boolean, False),
        "QueryStringsAllowList": ([str], False),
    }


class CacheSettings(AWSProperty):
    """
    `CacheSettings <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-cachesettings.html>`__
    """

    props: PropsDictType = {
        "AllowedHTTPMethods": (str, False),
        "CachedHTTPMethods": (str, False),
        "DefaultTTL": (integer, False),
        "ForwardedCookies": (CookieObject, False),
        "ForwardedHeaders": (HeaderObject, False),
        "ForwardedQueryStrings": (QueryStringObject, False),
        "MaximumTTL": (integer, False),
        "MinimumTTL": (integer, False),
    }


class InputOrigin(AWSProperty):
    """
    `InputOrigin <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-distribution-inputorigin.html>`__
    """

    props: PropsDictType = {
        "Name": (str, False),
        "ProtocolPolicy": (str, False),
        "RegionName": (str, False),
    }


class Distribution(AWSObject):
    """
    `Distribution <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-distribution.html>`__
    """

    resource_type = "AWS::Lightsail::Distribution"

    props: PropsDictType = {
        "BundleId": (str, True),
        "CacheBehaviorSettings": (CacheSettings, False),
        "CacheBehaviors": ([CacheBehaviorPerPath], False),
        "CertificateName": (str, False),
        "DefaultCacheBehavior": (CacheBehavior, True),
        "DistributionName": (str, True),
        "IpAddressType": (str, False),
        "IsEnabled": (boolean, False),
        "Origin": (InputOrigin, True),
        "Tags": (Tags, False),
    }


class DiskProperty(AWSProperty):
    """
    `DiskProperty <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-disk.html>`__
    """

    props: PropsDictType = {
        "AttachedTo": (str, False),
        "AttachmentState": (str, False),
        "DiskName": (str, True),
        "IOPS": (integer, False),
        "IsSystemDisk": (boolean, False),
        "Path": (str, True),
        "SizeInGb": (str, False),
    }


class Hardware(AWSProperty):
    """
    `Hardware <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-hardware.html>`__
    """

    props: PropsDictType = {
        "CpuCount": (integer, False),
        "Disks": ([DiskProperty], False),
        "RamSizeInGb": (integer, False),
    }


class MonthlyTransfer(AWSProperty):
    """
    `MonthlyTransfer <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-monthlytransfer.html>`__
    """

    props: PropsDictType = {
        "GbPerMonthAllocated": (str, False),
    }


class Port(AWSProperty):
    """
    `Port <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-port.html>`__
    """

    props: PropsDictType = {
        "AccessDirection": (str, False),
        "AccessFrom": (str, False),
        "AccessType": (str, False),
        "CidrListAliases": ([str], False),
        "Cidrs": ([str], False),
        "CommonName": (str, False),
        "FromPort": (integer, False),
        "Ipv6Cidrs": ([str], False),
        "Protocol": (str, False),
        "ToPort": (integer, False),
    }


class Networking(AWSProperty):
    """
    `Networking <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lightsail-instance-networking.html>`__
    """

    props: PropsDictType = {
        "MonthlyTransfer": (MonthlyTransfer, False),
        "Ports": ([Port], True),
    }


class Instance(AWSObject):
    """
    `Instance <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-instance.html>`__
    """

    resource_type = "AWS::Lightsail::Instance"

    props: PropsDictType = {
        "AddOns": ([AddOn], False),
        "AvailabilityZone": (str, False),
        "BlueprintId": (str, True),
        "BundleId": (str, True),
        "Hardware": (Hardware, False),
        "InstanceName": (str, True),
        "KeyPairName": (str, False),
        "Networking": (Networking, False),
        "Tags": (Tags, False),
        "UserData": (str, False),
    }


class LoadBalancer(AWSObject):
    """
    `LoadBalancer <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-loadbalancer.html>`__
    """

    resource_type = "AWS::Lightsail::LoadBalancer"

    props: PropsDictType = {
        "AttachedInstances": ([str], False),
        "HealthCheckPath": (str, False),
        "InstancePort": (integer, True),
        "IpAddressType": (str, False),
        "LoadBalancerName": (str, True),
        "SessionStickinessEnabled": (boolean, False),
        "SessionStickinessLBCookieDurationSeconds": (str, False),
        "Tags": (Tags, False),
        "TlsPolicyName": (str, False),
    }


class LoadBalancerTlsCertificate(AWSObject):
    """
    `LoadBalancerTlsCertificate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-loadbalancertlscertificate.html>`__
    """

    resource_type = "AWS::Lightsail::LoadBalancerTlsCertificate"

    props: PropsDictType = {
        "CertificateAlternativeNames": ([str], False),
        "CertificateDomainName": (str, True),
        "CertificateName": (str, True),
        "HttpsRedirectionEnabled": (boolean, False),
        "IsAttached": (boolean, False),
        "LoadBalancerName": (str, True),
    }


class StaticIp(AWSObject):
    """
    `StaticIp <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-staticip.html>`__
    """

    resource_type = "AWS::Lightsail::StaticIp"

    props: PropsDictType = {
        "AttachedTo": (str, False),
        "StaticIpName": (str, True),
    }
