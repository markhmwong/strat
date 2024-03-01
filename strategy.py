# Assuming python3 usage for interface implementation
# This will let you scale your code if additional api implementations are necessary
# just add the concrete class with it's own concrete algorithm. Determine what api method is used at "Main" and just instatiate and call execute

# ABC - Abstract Base Classes
from abc import ABC, abstractmethod 


class ApiUtil():

    def getApi():
        pass

    def deleteApi():
        pass

    def stopApi():
        pass

class ArtifactoryUtil():

    def update():
        pass

    def 

#create abstract base class. All apis should have a binding contract to these methods
class ApiDeploymentImplementation(ABC):

    @abstractmethod
    def run(self):
        pass
    
    @abstractmethod
    def readInputs():
        pass
    
    @abstractmethod
    def delete():
        pass

    @abstractmethod
    def rollback():
        pass

    @abstractmethod
    def backout():
        pass

    # add more common methods as necessary. some implementation

"""
Api deployment concrete classes
"""

class Db2(ApiDeploymentImplementation):
    def __init__(self, apiUtil: ApiUtil) -> None:
        print("This is db2")
        self.apiUtil = apiUtil

    def run(self):
        print("running db2")
        pass
    
    
    def readInputs():
        pass
    
    
    def delete():
        pass

    
    def rollback():
        pass

    
    def backout():
        pass

class Inbound(ApiDeploymentImplementation):

    def __init__(self, apiUtil: ApiUtil) -> None:
        print("This is inbound")
        self.apiUtil = apiUtil

    def run(self):
        print("running inbound")
        pass

    def readInputs():
        pass
    
    
    def delete():
        pass

    
    def rollback():
        pass

    
    def backout():
        pass

class Outbound(ApiDeploymentImplementation):

    def __init__(self, apiUtil: ApiUtil, artifactory: ArtifactoryUtil) -> None:
        print("This is outbound")
        self.apiUtil = apiUtil
        self.artifactoryUtil = artifactoryUtil

    def run(self):
        print("running outbound")
        pass

    def readInputs():
        pass
    
    
    def delete():
        apiUtil.getApi()
        apiUtil.stopApi()
        apiUtil.deleteApi()

    
    def rollback():
        pass

    
    def backout():
        pass



class ApiStrategy():

    def __init__(self, apiType: ApiDeploymentImplementation) -> None:
        self.apiType = apiType
    
    def deploy(self):
        self.apiType.run()

    def removeApi(self):
        self.apiType.delete()

    def publishApi(self):
        self.apiType

"""
Main stuff
"""

if __name__ == "__main__":
    apiType = "outbound"
    if apiType == "outbound":
        print("outbound")

        outboundStrat = ApiStrategy(Outbound(ApiUtil(), ArtifactoryUtil()))
        outboundStrat.deploy()
        inboundStrat = ApiStrategy(Inbound(ApiUtil()))
        inboundStrat.deploy()
        db2Strat = ApiStrategy(Db2(ApiUtil()))
        db2Strat.deploy()
