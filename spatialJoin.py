# -*- coding: utf-8 -*-

import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = "toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [Tool]


class Tool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Tool"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params0 = arcpy.Parameter(
            displayName="Input Features Class 1",
            name='in_features1',
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Input",
            multiValue=True
        )

        # params1 = arcpy.Parameter(
        #     displayName="Input Features Class 2",
        #     name='in_features2',
        #     datatype="GPFeatureLayer",
        #     parameterType="Required",
        #     direction="Input"
        # )

        # params2 = arcpy.Parameter(
        #     displayName="Input Features Class 3",
        #     name='in_features3',
        #     datatype="GPFeatureLayer",
        #     parameterType="Required",
        #     direction="Input"
        # )

        return [params0]

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""

        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        arcpy.env.workspace = r'C:\Users\test\Documents\ArcGIS\Projects\YFirstDemoTool\YFirstDemoTool.gdb'
        arcpy.env.overwriteOutput = True
        arcpy.env.addOutputsToMap = True
        #Taking Input Multipatch Layers From Users
        inFeatures      = parameters[0].valueAsText
        listOfInputFeatureClass = inFeatures.split(';')
        arcpy.AddMessage(listOfInputFeatureClass)

        #Converting From Mutipatch To 2D Layer For Spatial Join 
        for fc in listOfInputFeatureClass:
            # Determine if the feature class is a multipatch
            desc = arcpy.Describe(fc)
            if desc.shapeType == "MultiPatch":
                 arcpy.AddMessage(desc.shapeType)
                 #Execute MultiPatchFootprint
                 output = 'featureClass{0}'.format(desc.baseName)
                 arcpy.ddd.MultiPatchFootprint(fc, output)

        # desc1 = arcpy.Describe(values_to_remove[0])
        # dataType = desc1.datatype
        # arcpy.AddMessage(dataType)



        fcList2d = arcpy.ListFeatureClasses('featureClassLayer*')
        arcpy.AddMessage(fcList2d)
        

        # for fc in fcList2d:
            


        #Spatial Join 
        # arcpy.analysis.SpatialJoin(target_features, join_features, out_feature_class)


                  

        # arcpy.ddd.MultiPatchFootprint(inFeatures,'footprint1')

        # arcpy.AddMessage(inFeatures)
        # arcpy.AddMessage(inFeatures2)

        # result = arcpy.management.Merge([TargetFeatures, joinFeatures],o_fc, "ADD_SOURCE_INFO")

        # aprx = arcpy.mp.ArcGISProject('CURRENT')
        # for m in aprx.listMaps():
        #     arcpy.AddMessage("Map: " + m.name)
        #     for lyr in m.listLayers():
        #         arcpy.AddMessage("  " + lyr.name)
        #         arcpy.AddMessage(lyr.isFeatureLayer)

        # Map = aprx.listMaps('Scene')[0]
        # arcpy.AddMessage(Map)

        # featureLayer = arcpy.MakeFeatureLayer_management(
            # o_fc, 'op_featureLayer')
        # arcpy.AddMessage(featureLayer)

      

        # featureclasses = arcpy.ListFeatureClasses()
        # arcpy.AddMessage(featureclasses)

        # lyrFile = arcpy.mp.LayerFile(featureLayer)
        # arcpy.AddMessage(o_fc.isFeatureLayer)
        # lf = arcpy.mp.LayerFile(featureLayer)
        # lyr = Map.addLayer(lf)
        # aprx.save()
        # del aprx
        # arcpy.AddMessage(lyr)

        # desc1 = arcpy.Describe(r'C:\Users\test\Desktop\HY_Sample\HY_Sample\Enclosed_Multipatch\Enclose_Multipatch_D_Hydrabad_Part_1.gdb/Enclose_Multipatch_D_Hydrabad_Part_1')
        # geometryType = desc1.datatype
        # arcpy.AddMessage(geometryType)

        # desc2 = arcpy.Describe(r'C:\Users\test\Desktop\HY_Sample\HY_Sample\Enclosed_Multipatch\Enclose_Multipatch_UC_B1.gdb/Enclose_Multipatch_UC_B1')
        # base = desc2.datatype
        # arcpy.AddMessage(base)

        # desc3 = arcpy.Describe(r'C:\Users\test\Desktop\HY_Sample\HY_Sample\Enclosed_Multipatch\Enclose_Multipatch_D_Hydrabad_Part_1.gdb')
        # ot = desc3.datatype
        # arcpy.AddMessage(ot)

        # result = arcpy.Exists(o_fc)
        # arcpy.analysis.SpatialJoin(TargetFeatures,joinFeatures,o_fc)
        # arcpy.AddMessage(result)
       

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return
