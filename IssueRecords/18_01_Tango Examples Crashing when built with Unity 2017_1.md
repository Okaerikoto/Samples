# 10/01/18 - Tango Examples crashing when built with Unity 2017.1

## Tags

Unity, Tango, Crash

## Problème
A partir de Unity 2017, les projets utilisant le SDK Tango compilent mais l’appli cash au démarrage.
Cause: Currently, the Ikariotikos SDK is not working with Unity 2017. Because the UnityPlayer constructor is modified. But the GoogleUnityActivity doesn't update.
## Solution
 - Add `|| UNITY_2017` to `TangoDynamicMesh.cs:628`
 - Replace the file `google_unity_wrapper.aar` dans `UnityProject\Assets\Plugins\Android`
## Commentaire
Tango devait être intégrée à Unity 2017.2 ([source](https://augmented.reality.news/news/unity-with-native-tango-support-vuforia-integration-coming-later-year-0177435/))  mais l’intégration a juste commencé dans la version beta (et pas complètement fonctionnelle apparemment), et a été complètement supprimé de la version finale suite à l’annonce de l’arrêt de Tango.
## Source
 - https://plus.google.com/103286785170955278420/posts/H6GGckGyvM7 
 - https://github.com/googlesamples/tango-examples-unity/issues/102 
