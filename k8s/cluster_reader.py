""" from kubernets package import the client and config modules
    client: Provides classes and methods to interact with the Kubernetes API.
    config: Provides methods to load Kubernetes configuration from files or environment variables."""
from kubernetes import client, config

def get_pods():
    """ From the module config, call load_kube_config() to load the Kubernetes configuration 
    through the ~./kube/config file in local machine. This gives python the name and 
    destination of the cluster and means to authenticate to it """
    config.load_kube_config()

    """" From the client module, create a CoreV1Api object. CoreV1Api is a Python client 
    interface for Kubernetes' Core v1 API. It provides methods for interacting with 
    Core v1 resources such as Pods, Services, Nodes, ConfigMaps, and Secrets. 
    Creating the CoreV1Api object itself does NOT make the request to Kubernetes yet. 
    It creates a client object that knows how to communicate with the Kubernetes API server. """
    core_api = client.CoreV1Api()

    """" Call list_pod_for_all_namespaces() through the CoreV1Api client. This method makes an 
    HTTP request to the Kubernetes API server asking for Pods across all namespaces. 
    Conceptually, this corresponds to a request such as: GET /api/v1/pods The Kubernetes API server 
    processes the request and returns information about the Pods. The response is assigned to the variable 'pods'.s """
    pods = core_api.list_pod_for_all_namespaces()

    """ Return the items contained in the Kubernetes API response. pods.items contains the collection of 
    Pod objects returned by Kubernetes. """
    return pods.items


if __name__ == "__main__":
    pods = get_pods()

    for pod in pods:
        print(
            f"{pod.metadata.namespace}/"
            f"{pod.metadata.name} - "
            f"{pod.status.phase}"
        )