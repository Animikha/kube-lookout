""" from kubernets package import the client and config modules
    client: Provides classes and methods to interact with the Kubernetes API.
    config: Provides methods to load Kubernetes configuration from files or environment variables."""
from kubernetes import client, config

def get_pods():
    """ From the module config, call load_kube_config() to load the Kubernetes configuration 
    through the ~./kube/config file in local machine. This gives python the name and 
    destination of the cluster and means to authenticate to it """
    config.load_kube_config()

    """" From the module client, call CoreV1Api(), CoreV1Api() makes http request to the 
    kubernetes cluster's kube-apiserver and connect to its Core v1 API endpoint containing 
    pods, services, nodes etc. Here to assign it to variable core_api """
    core_api = client.CoreV1Api()

    """" From the Core V1 API endpoint, call list_pod_for_all_namespaces() to get 
    the pods of all namespaces. Assign it the variable to pods """
    pods = core_api.list_pod_for_all_namespaces()

    """ Return the contents of varible pods in alist format"""
    return pods.items


if __name__ == "__main__":
    pods = get_pods()

    for pod in pods:
        print(
            f"{pod.metadata.namespace}/"
            f"{pod.metadata.name} - "
            f"{pod.status.phase}"
        )