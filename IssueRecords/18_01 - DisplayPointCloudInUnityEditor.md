# 10/01/18 - Affichage d’un nuage de points dans l’éditeur Unity

## Problème 

Impossible d’imposer la taille des points PSize avec un shader dans l’éditeur, tandis que cela marche dans l’appli compilée.

## Cause 

The problem is that for PSIZE to work in a vertex shader on OpenGL, you need to enable the GL_VERTEX_PROGRAM_POINT_SIZE feature using glEnable(). Unity doesn't do that by default, even though Direct3D always has it enabled and enabling it for OpenGL would bring functional parity between the two APIs. I posted a feature request for this on the Unity Feedback forum once, but never got any response.
In any case, I figured out a workaround for this by using P/Invoke to call glEnable directly before rendering.

## Solution

Lancer Unity de cette manière : `.\Unity.exe -force-opengl`
Ajouter ce script à la caméra :
```
#if UNITY_STANDALONE
#define IMPORT_GLENABLE
#endif
 
using UnityEngine;
using System;
using System.Collections;
using System.Runtime.InteropServices;
 
public class EnablePointSize : MonoBehaviour 
{
    const UInt32 GL_VERTEX_PROGRAM_POINT_SIZE = 0x8642;
    const UInt32 GL_POINT_SMOOTH = 0x0B10;
     
    const string LibGLPath =
        #if UNITY_STANDALONE_WIN
        "opengl32.dll";
    #elif UNITY_STANDALONE_OSX
    "/System/Library/Frameworks/OpenGL.framework/OpenGL";
    #elif UNITY_STANDALONE_LINUX
    "libGL";  // Untested on Linux, this may not be correct
    #else
    null;   // OpenGL ES platforms don't require this feature
    #endif
     
    #if IMPORT_GLENABLE
    [DllImport(LibGLPath)]
    public static extern void glEnable(UInt32 cap);
     
    private bool mIsOpenGL;
     
    void Start()
    {
        mIsOpenGL = SystemInfo.graphicsDeviceVersion.Contains("OpenGL");
    }
     
    void OnPreRender()
    {
        if (mIsOpenGL)
            glEnable(GL_VERTEX_PROGRAM_POINT_SIZE);
            glEnable(GL_POINT_SMOOTH);
    }
    #endif
}
```
 
## Commentaires

I figured out a workaround for this by using P/Invoke to call glEnable directly before rendering. You can simply add this script to a Camera game object and it should work.
It's tested and working on both Windows and Mac; Linux should work as well but remains untested. As you can see I also added a check to see if we're actually running in OpenGL mode, so we don't inadvertently end up loading the OpenGL library when we're in Direct3D.
I also tested it for OpenGL ES on Android and iOS, but it looks like GL_VERTEX_PROGRAM_POINT_SIZE does not exist there, and while setting the PSIZE register did have some effect, it caused all sorts of random glitchiness. I'll have to investigate further to see if there's some way to get this working on OpenGL ES. 


## Picture

Figure 1: Après résolution du problème (avant, on ne voit pas les points)
![alt text](https://github.com/Okaerikoto/Samples/ IssueRecords/point_cloud.png "Logo Title Text 1After resolving the issue")
 
## Sources

 - http://www.kamend.com/2014/05/rendering-a-point-cloud-inside-unity/  (01/2018)
 - https://answers.unity.com/questions/519670/shader-inconsistency-between-opengl-and-directx.html (01/2018)


