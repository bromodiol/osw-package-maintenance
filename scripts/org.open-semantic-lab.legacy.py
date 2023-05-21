from pathlib import Path

from reusable import OslCreat, OslMeta

# Provide information on the page package to be created
package_meta_data = OslMeta(
    # Package name
    name="OSL Legacy Core",
    # Package repository name - usually the GitHub repository name
    repo="org.open-semantic-lab.legacy",
    # Package ID - usually the same as repo
    id="org.open-semantic-lab.legacy.core",
    # Package subdirectory - usually resembling parts of the package name
    subdir="core",
    # Package branch - usually "main"
    branch="main",
    # Provide a package description
    description=("Provides core functionalities of OpenSemanticLab < 0.2.0"),
    # Specify the package version - use semantic versioning
    version="0.1.0",
    # Author(s)
    author=["Simon Stier"],
    # List the full page titles of the pages to be included in the package
    # You can include a comment in the same line, stating the page label
    page_titles=[
        "Category:Data",
        "Category:DataProperty",
        "Category:DataSet",
        "Category:Device",
        "Category:File",
        "Category:Material",
        "Category:ObjectProperty",
        "Category:OSL",
        "Category:OSL/Infrastructure",
        "Category:OSL/Infrastructure/Messages",
        "Category:OSL/Infrastructure/Template",
        "Category:OSL/Infrastructure/Template/User",
        "Category:OSL/Property",
        "Category:QuantityProperty",
        "Category:Software",
        "Category:Tool",
        "Concept:ELN/Entry/Creator",
        "Concept:ELN/Order/Creator",
        "Concept:LIMS/Device/Category",
        "Concept:LIMS/Device/Instance",
        "Concept:LIMS/Device/Type",
        "Concept:LIMS/File/Category",
        "Concept:LIMS/Location/Instance",
        "Concept:LIMS/Material/Category",
        "Concept:LIMS/Object/Category",
        "Concept:LIMS/Ou",
        "Concept:LIMS/Property/Category",
        "Concept:LIMS/Software/Category",
        "Form:ELN",
        "Form:ELN/Editor/ParamSet",
        "Form:ELN/Entry",
        "Form:ELN/Entry/Query",
        "Form:ELN/Order",
        "Form:ELN/Order/Actionable",
        "Form:ELN/Order/Actionable/Query",
        "Form:ELN/Order/Query",
        "Form:KB/Class",
        "Form:KB/Entity",
        "Form:KB/Term",
        "Form:LabProcess",
        "Form:LabProcess/Instance",
        "Form:LabProcess/Query/InteractiveSemanticGraph",
        "Form:LabProcess/Steps",
        "Form:LabProcess/Steps/Generic",
        "Form:LabProcess/Steps/GravimetricDosing",
        "Form:LabProcess/Steps/MultiObjectSelection",
        "Form:LabProcess/Steps/ObjectSelection",
        "Form:LIMS",
        "Form:LIMS/ACL",
        "Form:LIMS/Device",
        "Form:LIMS/Device/Category",
        "Form:LIMS/Device/Instance",
        "Form:LIMS/Device/Type",
        "Form:LIMS/File/Category",
        "Form:LIMS/File/Type",
        "Form:LIMS/Location/Building",
        "Form:LIMS/Location/Floor",
        "Form:LIMS/Location/Room",
        "Form:LIMS/Location/Site",
        "Form:LIMS/Material",
        "Form:LIMS/Material/Category",
        "Form:LIMS/Material/Instance",
        "Form:LIMS/Material/Type",
        "Form:LIMS/Ou",
        "Form:LIMS/Ou/Organization",
        "Form:LIMS/Ou/Organization/Query",
        "Form:LIMS/Person",
        "Form:LIMS/Person/Query",
        "Form:LIMS/Person/User",
        "Form:LIMS/Query/Device",
        "Form:LIMS/Software/Category",
        "Form:LIMS/Software/Instance",
        "Form:LIMS/Software/Type",
        "Form:Property",
        "Form:Property/Quantity",
        "Form:Property/Subquantity",
        "MediaWiki:Smw service cas",
        "MediaWiki:Smw service online maps",
        "MediaWiki:Smw service pubchem cid",
        "Module:KB/Viewer/SparqlGraph",
        "Module:LabProcess/Object",
        "Module:LabProcess/Parameter/Config",
        "OslTemplate:Common/Form/Label/Instances",
        "OslTemplate:Common/Label",
        "OslTemplate:ELN",
        "OslTemplate:ELN/Attachment",
        "OslTemplate:ELN/Attachment/TimeStamp",
        "OslTemplate:ELN/Attachment/TimeStampedDoc",
        "OslTemplate:ELN/Attachment/Verification",
        "OslTemplate:ELN/Attachment/Verification/TableBody",
        "OslTemplate:ELN/Attachment/Verification/TableFooter",
        "OslTemplate:ELN/Attachment/Verification/TableHeader",
        "OslTemplate:ELN/Decoration",
        "OslTemplate:ELN/Decoration/Annotation",
        "OslTemplate:ELN/Decoration/ColoredText",
        "OslTemplate:ELN/Editor",
        "OslTemplate:ELN/Editor/DrawIO",
        "OslTemplate:ELN/Editor/Graph",
        "OslTemplate:ELN/Editor/Kekule",
        "OslTemplate:ELN/Editor/Kekule/Default",
        "OslTemplate:ELN/Editor/ParamSet/Link",
        "OslTemplate:ELN/Editor/ParamSet/Subpage",
        "OslTemplate:ELN/Editor/Spreadsheet",
        "OslTemplate:ELN/Editor/SvgEdit",
        "OslTemplate:ELN/Editor/Wellplate",
        "OslTemplate:ELN/Entry",
        "OslTemplate:ELN/Entry/Body",
        "OslTemplate:ELN/Entry/Footer",
        "OslTemplate:ELN/Entry/Header",
        "OslTemplate:ELN/Entry/Query",
        "OslTemplate:ELN/Order",
        "OslTemplate:ELN/Order/Actionable",
        "OslTemplate:ELN/Order/Actionable/Query",
        "OslTemplate:ELN/Order/Body",
        "OslTemplate:ELN/Order/Footer",
        "OslTemplate:ELN/Order/Query",
        "OslTemplate:ELN/Order/Sample",
        "OslTemplate:ELN/Viewer",
        "OslTemplate:ELN/Viewer/Kekule",
        "OslTemplate:ELN/Viewer/ProjectTree",
        "OslTemplate:ELN/Viewer/Wellplate",
        "OslTemplate:Helper",
        "OslTemplate:Helper/Docu/FormTemplate",
        "OslTemplate:Helper/Id/BasePageSubobject",
        "OslTemplate:Helper/Id/RootPageSubobject",
        "OslTemplate:Helper/Id/RootPageSubobject/AsInput",
        "OslTemplate:Helper/Id/Subobject",
        "OslTemplate:Helper/Links",
        "OslTemplate:Helper/Links/ParamLink",
        "OslTemplate:Helper/Location/CustomMarker",
        "OslTemplate:Helper/Query",
        "OslTemplate:Helper/Query/DebugProperty",
        "OslTemplate:Helper/Query/List/SubPageList",
        "OslTemplate:Helper/Query/List/SubPageName",
        "OslTemplate:Helper/Query/Plain",
        "OslTemplate:Helper/Semantics/InlineProperty",
        "OslTemplate:Helper/Semantics/InlineProperty/DensityTooltip",
        "OslTemplate:Helper/Semantics/InlineProperty/HasChemicalStructureSDS",
        "OslTemplate:Helper/Semantics/InlineProperty/HasDensity",
        "OslTemplate:Helper/Semantics/InlineProperty/HasHazardStatement",
        "OslTemplate:Helper/Semantics/InlineProperty/HazardStatementTooltip",
        "OslTemplate:Helper/StringOps",
        "OslTemplate:Helper/StringOps/ConcatLists",
        "OslTemplate:Helper/StringOps/SplitOnTripleHashSelectFirst",
        "OslTemplate:Helper/Strings",
        "OslTemplate:Helper/Strings/CleanDisplayTitle",
        "OslTemplate:Helper/Strings/EqualSign",
        "OslTemplate:Helper/Strings/No",
        "OslTemplate:Helper/Strings/Yes",
        "OslTemplate:Helper/UI/Div/Closing",
        "OslTemplate:Helper/UI/Div/VE-Hidden",
        "OslTemplate:Helper/UI/Div/VE-Visible",
        "OslTemplate:Helper/UI/Tiles/Grid",
        "OslTemplate:Helper/UI/Tiles/Tile",
        "OslTemplate:Helper/UI/VE",
        "OslTemplate:Helper/UI/VE/EditButton",
        "OslTemplate:Helper/UI/VE/Hidden",
        "OslTemplate:Helper/UI/VE/SectionSeparator",
        "OslTemplate:Helper/UI/VE/SectionSeparatorHelper",
        "OslTemplate:Helper/UI/VE/Visible",
        "OslTemplate:ID",
        "OslTemplate:ID/Local",
        "OslTemplate:ID/UUID",
        "OslTemplate:ID/UUID/Format/Normal",
        "OslTemplate:ID/UUID/Format/Normal/Process",
        "OslTemplate:KB",
        "OslTemplate:KB/Attachment",
        "OslTemplate:KB/Class",
        "OslTemplate:KB/Relation",
        "OslTemplate:KB/Relation/ReverseListFormat",
        "OslTemplate:KB/Term",
        "OslTemplate:KB/Term/Body",
        "OslTemplate:KB/Term/Footer",
        "OslTemplate:KB/Viewer/GraphFromList",
        "OslTemplate:LabProcess",
        "OslTemplate:LabProcess/CreateInstanceLink",
        "OslTemplate:LabProcess/File",
        "OslTemplate:LabProcess/Footer",
        "OslTemplate:LabProcess/Header",
        "OslTemplate:LabProcess/Instance",
        "OslTemplate:LabProcess/Instance/Demo1",
        "OslTemplate:LabProcess/Instance/Footer",
        "OslTemplate:LabProcess/Instance/Header",
        "OslTemplate:LabProcess/Object",
        "OslTemplate:LabProcess/Object/Array",
        "OslTemplate:LabProcess/Object/ById",
        "OslTemplate:LabProcess/Object/ByName",
        "OslTemplate:LabProcess/Object/Global",
        "OslTemplate:LabProcess/Object/Id",
        "OslTemplate:LabProcess/Object/ObjectCreator",
        "OslTemplate:LabProcess/Object/Reference",
        "OslTemplate:LabProcess/Object/WikiId",
        "OslTemplate:LabProcess/Parameter",
        "OslTemplate:LabProcess/Parameter/MultiFile/Config",
        "OslTemplate:LabProcess/Parameter/MultiFile/File",
        "OslTemplate:LabProcess/Parameter/MultiFile/ParamArray",
        "OslTemplate:LabProcess/Parameter/MultiObject",
        "OslTemplate:LabProcess/Parameter/MultiObject/Config",
        "OslTemplate:LabProcess/Parameter/MultiObject/Object",
        "OslTemplate:LabProcess/Parameter/MultiObject/ParamArray",
        "OslTemplate:LabProcess/Parameter/MultiQuantitative",
        "OslTemplate:LabProcess/Parameter/MultiQuantitative/Config",
        "OslTemplate:LabProcess/Parameter/MultiQuantitative/ParamArray",
        "OslTemplate:LabProcess/Parameter/MultiQuantitative/Quantitative",
        "OslTemplate:LabProcess/Parameter/MultiTool",
        "OslTemplate:LabProcess/Parameter/MultiTool/Config",
        "OslTemplate:LabProcess/Parameter/MultiTool/Device",
        "OslTemplate:LabProcess/Parameter/MultiTool/Tool",
        "OslTemplate:LabProcess/Parameter/Tool",
        "OslTemplate:LabProcess/Query",
        "OslTemplate:LabProcess/Query/DeviceParam",
        "OslTemplate:LabProcess/Query/GenericParam",
        "OslTemplate:LabProcess/Query/GenericParam/SubQuery",
        "OslTemplate:LabProcess/Query/InteractiveSemanticGraph",
        "OslTemplate:LabProcess/Query/Param",
        "OslTemplate:LabProcess/Step",
        "OslTemplate:LabProcess/Step/Descriptor",
        "OslTemplate:LabProcess/Step/Footer",
        "OslTemplate:LabProcess/Step/Form",
        "OslTemplate:LabProcess/Step/Form/Footer",
        "OslTemplate:LabProcess/Step/Form/Header",
        "OslTemplate:LabProcess/Step/Form/Param",
        "OslTemplate:LabProcess/Step/Form/Param/Common",
        "OslTemplate:LabProcess/Step/Form/Param/Material",
        "OslTemplate:LabProcess/Step/Form/Param/Material/Fields",
        "OslTemplate:LabProcess/Step/Form/Param/Material/Footer",
        "OslTemplate:LabProcess/Step/Form/Param/Material/Header",
        "OslTemplate:LabProcess/Step/Form/Param/Multi",
        "OslTemplate:LabProcess/Step/Form/Param/Multi/Header",
        "OslTemplate:LabProcess/Step/Form/Param/Multi/SectionHeader",
        "OslTemplate:LabProcess/Step/Form/Param/MultiFile/Fields",
        "OslTemplate:LabProcess/Step/Form/Param/MultiFile/Rows",
        "OslTemplate:LabProcess/Step/Form/Param/MultiObject",
        "OslTemplate:LabProcess/Step/Form/Param/MultiObject/Fields",
        "OslTemplate:LabProcess/Step/Form/Param/MultiObject/Rows",
        "OslTemplate:LabProcess/Step/Form/Param/MultiQuantitative",
        "OslTemplate:LabProcess/Step/Form/Param/MultiQuantitative/Fields",
        "OslTemplate:LabProcess/Step/Form/Param/MultiQuantitative/Rows",
        "OslTemplate:LabProcess/Step/Form/Param/MultiTool",
        "OslTemplate:LabProcess/Step/Form/Param/MultiTool/Fields",
        "OslTemplate:LabProcess/Step/Form/Param/MultiTool/Rows",
        "OslTemplate:LabProcess/Step/Form/Param/Object",
        "OslTemplate:LabProcess/Step/Form/Param/Object/Fields",
        "OslTemplate:LabProcess/Step/Form/Param/Object/Footer",
        "OslTemplate:LabProcess/Step/Form/Param/Object/Header",
        "OslTemplate:LabProcess/Step/Form/Param/Quantitative",
        "OslTemplate:LabProcess/Step/Form/Param/Quantitative/Fields",
        "OslTemplate:LabProcess/Step/Form/Param/Quantitative/Footer",
        "OslTemplate:LabProcess/Step/Form/Param/Quantitative/Header",
        "OslTemplate:LabProcess/Step/Form/Param/Specific",
        "OslTemplate:LabProcess/Step/Form/Param/Specific/Footer",
        "OslTemplate:LabProcess/Step/Form/Param/Specific/Header",
        "OslTemplate:LabProcess/Step/Form/Param/Tool",
        "OslTemplate:LabProcess/Step/Form/Param/Tool/Fields",
        "OslTemplate:LabProcess/Step/Form/Param/Tool/Footer",
        "OslTemplate:LabProcess/Step/Form/Param/Tool/Header",
        "OslTemplate:LabProcess/Step/Subpage",
        "OslTemplate:LabProcess/Step/Subpage/Template",
        "OslTemplate:LabProcess/Steps",
        "OslTemplate:LabProcess/Steps/Generic",
        "OslTemplate:LabProcess/Steps/Generic/Subpage",
        "OslTemplate:LabProcess/Steps/GravimetricDosing",
        "OslTemplate:LabProcess/Steps/GravimetricDosing/Subpage",
        "OslTemplate:LabProcess/Steps/MultiObjectSelection",
        "OslTemplate:LabProcess/Steps/MultiObjectSelection/Subpage",
        "OslTemplate:LabProcess/Steps/ObjectSelection",
        "OslTemplate:LabProcess/Steps/ObjectSelection/Subpage",
        "OslTemplate:LabProcess/Template/IoMapping",
        "OslTemplate:LIMS",
        "OslTemplate:LIMS/ACL",
        "OslTemplate:LIMS/ACL/Display",
        "OslTemplate:LIMS/Attachment",
        "OslTemplate:LIMS/Common",
        "OslTemplate:LIMS/Common/Category/Footer",
        "OslTemplate:LIMS/Common/Category/Header",
        "OslTemplate:LIMS/Common/Link",
        "OslTemplate:LIMS/Common/Property",
        "OslTemplate:LIMS/Common/Template",
        "OslTemplate:LIMS/Common/Viewer/LocationTree",
        "OslTemplate:LIMS/Device",
        "OslTemplate:LIMS/Device/Category",
        "OslTemplate:LIMS/Device/Instance",
        "OslTemplate:LIMS/Device/Type",
        "OslTemplate:LIMS/Device/Type/Body",
        "OslTemplate:LIMS/Device/Type/Footer",
        "OslTemplate:LIMS/File/Category",
        "OslTemplate:LIMS/File/Instance",
        "OslTemplate:LIMS/File/Type",
        "OslTemplate:LIMS/Form/Common",
        "OslTemplate:LIMS/Form/Common/Category/Header",
        "OslTemplate:LIMS/Form/Common/Footer",
        "OslTemplate:LIMS/Form/Common/Header",
        "OslTemplate:LIMS/Location/Building",
        "OslTemplate:LIMS/Location/Floor",
        "OslTemplate:LIMS/Location/Room",
        "OslTemplate:LIMS/Location/Site",
        "OslTemplate:LIMS/Material/Category",
        "OslTemplate:LIMS/Material/Instance",
        "OslTemplate:LIMS/Material/Type",
        "OslTemplate:LIMS/Ou",
        "OslTemplate:LIMS/Ou/Organization",
        "OslTemplate:LIMS/Ou/Organization/Query",
        "OslTemplate:LIMS/Person",
        "OslTemplate:LIMS/Person/Query",
        "OslTemplate:LIMS/Person/User",
        "OslTemplate:LIMS/Project/Part/Footer",
        "OslTemplate:LIMS/Project/Part/Header",
        "OslTemplate:LIMS/Query/Device",
        "OslTemplate:LIMS/Software/Category",
        "OslTemplate:LIMS/Software/Instance",
        "OslTemplate:LIMS/Software/Type",
        "OslTemplate:Message",
        "OslTemplate:Message/NotDefined",
        "OslTemplate:Property",
        "OslTemplate:Property/Quantitative",
        "OslTemplate:Property/Quantity",
        "OslTemplate:Property/Quantity/Unit",
        "OslTemplate:Test",
        "Template:ELN/Decoration/Annotation",
        "Template:ELN/Decoration/ColoredText",
        "Template:ELN/Editor/DrawIO",
        "Template:ELN/Editor/Graph",
        "Template:ELN/Editor/Kekule",
        "Template:ELN/Editor/Spreadsheet",
        "Template:ELN/Editor/SvgEdit",
        "Template:ELN/Editor/Wellplate",
        "Template:ELN/Viewer/Kekule",
        "Template:ELN/Viewer/ProjectTree",
        "Template:LIMS/Common/Viewer/LocationTree",
        "Template:ELN/Editor/ParamSet",
        "OslTemplate:ELN/Editor/ParamSet",
        "CreatePage",
        "Category:Object",
        "Category:Thing",
        "Category:Process",
        "Category:Term",
        "Category:LIMS/Person/User",
        "Category:LIMS/Person",
    ],
)
# Provide the information needed (only) to create the page package
package_creation_config = OslCreat(
    # Specify the path to the working directory - where the package is stored on disk
    working_dir=Path(__file__).parents[1]
    / "packages"
    / package_meta_data.repo,
)
# Create the page package
package_meta_data.create(
    creation_config=package_creation_config,
)

# Todo: check if the following deviating lines are needed:
# baseURL = f"https://raw.githubusercontent.com/{package_repo_org}/{package_repo}/main/{package_name}",
# config_path=os.path.join(working_dir, f"{package_name}_packages.json"),