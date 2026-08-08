import random
from comgen.enums import Race, Rank, Sex, Subtype


class ComGen:
    """
    A class to generate a commanders portraits and names.
    
    """

    def __init__(self, options):
        """
        Generate commanders portraits and names based on the provided parameters.        
        
        Args:
            params (collection): Generation options provided
        
        Returns:
            list: Return a list of `ComGen` object containing all the commanders attributes 
        """

        params = self.getCommandersParams(options)

    def generateCommander(self, params):
        """
        Generates a commander based on the provided parameters.
        
        Returns:
            dict: A dictionary containing the generated commander's attributes
        """

    def getCommandersParams(self, options):
        """
        Returns the Parameters for each commanders to generate.
        
        Args:
            options (collection): Generation options provided

        Returns:
            params (list): A List of collections of parameters for each commander to generate
        """

        #If their is unset options, randomize them for each commander
        params = []
        param = {
            "race": Race.get(Race.getTitle().index(options["race"])+1),
        }
        for i in range(options["batch"]):
            if options["sex"] == "":
                param["sex"] = random.choice(Sex.list())
            else:
                param["sex"] = Sex.get(Sex.getTitle().index(options["sex"])+1)

            if options["subtype"] == "":
                param["subtype"] = random.choice(Subtype.list())
            else:
                param["subtype"] = Subtype.get(Subtype.getTitle().index(options["subtype"])+1)

            if options["rank"] == "":
                param["rank"] = random.choice(Rank.list())
            else:
                param["rank"] = Rank.get(Rank.getTitle().index(options["rank"])+1)

            params.append(param.copy())

        return params
