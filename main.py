# diagram.py
from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

from diagrams.k8s.clusterconfig import HPA
from diagrams.k8s.compute import Pod, ReplicaSet, Deployment
from diagrams.k8s.network import Service, Ingress


# Diagram name and file
with Diagram("Web Service", show=False):
    with Cluster('App cluster'):
        ELB("lb") >> EC2("web") >> RDS("userdb")
        ELB("lb") >> EC2("web") >> RDS("userdb")
    
    with Cluster("App 2"):
        net = Ingress("domain.com") >> Service("svc")
        net >> [
            Pod("pod1"),
            Pod("pod2"),
            Pod("pod3")
        ] << ReplicaSet("rs") << Deployment("dp") << HPA("hpa")
