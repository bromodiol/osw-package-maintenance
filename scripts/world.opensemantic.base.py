from pathlib import Path

from reusable import WorldCreat, WorldMeta

# Provide information on the page package to be created
package_meta_data = WorldMeta(
    # Package name
    name="OSW Base",
    # Package repository name - usually the GitHub repository name
    repo="world.opensemantic.base",
    # Package ID - usually the same as repo
    id="world.opensemantic.base",
    # Package subdirectory - usually resembling parts of the package name
    subdir="base",
    # Package branch - usually "main"
    branch="main",
    # Provide a package description
    description=("Provides base items like Article, Person, Project"),
    # Specify the package version - use semantic versioning
    version="0.19.0",
    # Specify the required PagePackages
    requiredPackages=[
        "world.opensemantic.core",
    ],
    # Author(s)
    author=["Simon Stier", "Lukas Gold", "Matthias Albert Popp", "Alexander Triol"],
    # List the full page titles of the pages to be included in the package
    # You can include a comment in the same line, stating the page label
    page_titles=[
        "Category:OSW712583f2479944deb2546b77cf860dda",  # Creative Work
        "Category:OSW92cc6b1a2e6b4bb7bad470dfdcfdaf26",  # Article
        "Category:OSWe2c50b1034684c1b9a5c21ad371d6381",  # How To
        "Category:OSW494f660e6a714a1a9681c517bbb975da",  # Tutorial
        "Category:OSW0e084decca6f48a7b023d6b7b2c1452d",  # Event
        "Category:OSW81e9e22e7d934382a6a56df7d3736957",  # Recipe
        "Category:OSWfe72974590fd4e8ba94cd4e8366375e8",  # DataSet
        "Category:OSW3d238d05316e45a4ac95a11d7b24e36b",  # Location
        "Category:OSW473d7a1ed48544d1be83b258b5810948",  # Site
        "Category:OSW4bcd4a99a73f482ea40ac4210dfab836",  # Building
        "Category:OSW6c4212f1a39342be963d2b9efd19c5c2",  # Floor
        "Category:OSWc5ed0ed1e33c4b31887c67af25a610c1",  # Room
        "Category:OSW137e7443b2b94692bd59a0e0a6778b70",  # Administrative Area
        "Category:OSW0551abcd6f734047825e3ded4c8a0ffe",  # Country
        "Category:OSWab60f9a227954ee0be92344ff6272420",  # State
        "Category:OSW807f1da5b42e42f296b213ab06ca873b",  # City
        "Category:OSW95efaf34e2c7439e8e7967233910e44b",  # Region
        "Category:OSWd845b96813a344458f140e48c4d063fd",  # MetaDeviceCategory
        "Category:OSWf0fe562f422d49c6877490b3dfee2f3f",  # Device
        "Category:OSWfa0d5710bc0f45819b61b65fc4fd9656",  # StrictParticipantsProcess
        "Category:OSW1a271f289649413488e2841580e43a45",  # AdministrativeProcess
        "Category:OSW3886740859ae459588fee73d3bb3c83e",  # RiskAssessmentProcess ToDo: maybe to specific
        "Category:OSW02590972aeba46d7864ed492c0c11384",  # Host
        "Category:OSW77e749fc598341ac8b6d2fff21574058",  # Software
        "Category:OSW8c56fd1e858f499da801691c5f2b7309",  # WebService
        "Category:OSWb2d7e6a2eff94c82b7f1f2699d5b0ee3",  # Project
        "Category:OSW490e38f9764f4408a244869a0ea98e7c",  # Project (Application) Status
        "Category:OSW595b282aedf048788f3ee326454792ce",  # Budget Type
        "Category:OSW25bc4daf97644737a76434b88e1d5b21",  # Grant
        "Category:OSWbe80b28aefd64921ba2e8e2d6225416e",  # Monetary Grant
        "Category:OSWd22af0aa3b00462a9da9b509538e8926",  # FundingCall
        "Category:OSWac9f0e49d8024804bd7d77058322a3fe",  # RoomUsage
        "Category:OSWae92be81cdb34d22844d4791ef790d93",  # AreaUsageType
        "Category:OSW44deaa5b806d41a2a88594f562b110e9",  # Person
        "Category:OSWd9aa0bca9b0040d8af6f5c091bf9eec7",  # User
        "Category:OSW3cb8cef2225e403092f098f99bc4c472",  # OrganizationalUnit
        "Category:OSW1969007d5acf40539642877659a02c23",  # Organization
        "Category:OSW9d63242855e44ab8b26d6ad9792a67b3",  # Educational Organization
        "Category:OSWcffdc90247c142eca7f23ab6c69e49a1",  # NonGovernmentalOrganization
        "Category:OSWd9521d3054814dd29c2bcdbd9185d1f0",  # Association
        "Category:OSW5f4a3751d23e482d80fb0b72dcd6bc31",  # Corporation
        "Category:OSWd7085ef89b0e4a69ac4f2d28bda2d2c0",  # Foundation
        "Category:OSW11ee14fb9f774b4b89bdb9bb89aac14d",  # University
        "Category:OSWfe3e842b804445c7bb0dd8ee61da2d70",  # OrganizationalSubUnit
        "Category:OSW94aa074255374580b70337340c5ccc1b",  # Department
        "Category:OSWa01126bc9e9048988cb0f49e359015bc",  # Faculty
        "Category:OSWb8b6278763d54b0784eea9d3b3d183a4",  # Group
        "Category:OSW5427361692374c8eaa6bd3733b92d343",  # Institute
        "Category:OSW51653bb12c534c0b92a255b0b5ca3984",  # Function
        "Category:OSW5efde23b1d8c4e1c864ef039cb0616ed",  # PersonRole
        "Category:OSW07a0faef5be94b788514a2dd5dca20bf",  # BuildingFunction
        "Category:OSW5a13eeda5ed5405ea7ef62ea6feeceec",  # Topic
        "Category:OSW5eb9c52b804544dc870dfd54ff434428",  # Competence
        "Category:OSW8cb1935054464c99836d3bc0573a11cc",  # Issue Label
        "Category:OSW973a5cd08ea14524a57089f0b3c9c6ff",  # Requirement
        "Item:OSWab093fd8af104a49882704cea3bbaf7b",  # FunctionalRequirement
        "Item:OSWbb07a72940554b1b978c44e5db4bd314",  # NonFunctionalRequirement
        "Item:OSW55a9a9bda7b248759e48ae2e3ed6df1d",  # Ongoing
        "Template:Editor/Requirements",
        "Property:HasId",
        "Property:IsRelatedTo",
        "Property:HasPhoneNumber",
        "Property:HasApprover",
        "Property:HasOrderer",
        "Property:HasContact",
        "Property:HasUrl",
        "Property:HasVersion",
        "Property:HasManufacturer",
        "Property:HasManual",
        # "Property:HasPurpose",
        "Property:HasResponsiblePerson",
        "Property:IsLocatedIn",
        "Property:HasDepartment",
        # "Property:HasDatabase",
        "Property:HasInventoryNumber",
        # "Property:HasMeasurementChannels",
        "Property:HasRiskAssessment",
        "Property:HasOwner",
        "Property:HasSerialNumber",
        "Property:HasNetworkDomain",
        "Property:HasIp4Address",
    ],
)
# Provide the information needed (only) to create the page package
package_creation_config = WorldCreat(
    # Specify the path to the working directory - where the package is stored on disk
    working_dir=Path(__file__).parents[1]
    / "packages"
    / package_meta_data.repo,
)

if __name__ == "__main__":
    # Create the page package
    package_meta_data.create(
        creation_config=package_creation_config,
    )
    # Check if all required pages are present
    package_meta_data.check_required_pages(
        params=WorldMeta.CheckRequiredPagesParams(
            creation_config=package_creation_config,
            # Enable the following line to use the package creation script for the
            #  check of listed pages in the requiredPackages instead of the
            #  package.json (which is only up-to-date after the execution of the
            #  package creation script)
            read_listed_pages_from_script=True,
            script_dir=Path(__file__).parent,
        )
    )
