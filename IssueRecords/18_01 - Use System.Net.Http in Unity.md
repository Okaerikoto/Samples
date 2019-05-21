# 15/01/18 - Use System.Net.Http in Unity

## Tags  
Unity, .Net, Http
## Problème
System.Net.Http library not reconised in Unity 2017.2.0p4
## Cause 
This library was not supported in .NET 3.5 framework.
## Solution

### 1. Utiliser les pluggins Unity suivants :

- [**http Client**](https://assetstore.unity.com/packages/tools/network/http-client-79343/reviews)
  - Utiliser des coroutines pour attendre les appels de réponse : (link)[https://stackoverflow.com/questions/48303985/how-to-wait-for-a-callback-before-returning]
  - Autoriser tous les certificats, sinon le post ne marche pas:
     - Just add the following line before making your request:			
    `ServicePointManager.ServerCertificateValidationCallback = MyRemoteCertificateValidationCallback;`			
     - And this method:
```
public bool MyRemoteCertificateValidationCallback(System.Object sender, X509Certificate certificate, X509Chain chain, SslPolicyErrors sslPolicyErrors)
{
    bool isOk = true;
    // If there are errors in the certificate chain,
    // look at each error to determine the cause.
    if (sslPolicyErrors != SslPolicyErrors.None) {
        for (int i=0; i<chain.ChainStatus.Length; i++) {
            if (chain.ChainStatus[i].Status == X509ChainStatusFlags.RevocationStatusUnknown) {
                continue;
            }
            chain.ChainPolicy.RevocationFlag = X509RevocationFlag.EntireChain;
            chain.ChainPolicy.RevocationMode = X509RevocationMode.Online;
            chain.ChainPolicy.UrlRetrievalTimeout = new TimeSpan (0, 1, 0);
            chain.ChainPolicy.VerificationFlags = X509VerificationFlags.AllFlags;
            bool chainIsValid = chain.Build ((X509Certificate2)certificate);
            if (!chainIsValid) {
                isOk = false;
                break;
            }
        }
    }
    return isOk;
}
```			
  - [link](https://stackoverflow.com/questions/4926676/mono-https-webrequest-fails-with-the-authentication-or-decryption-has-failed)
			
- [**HttpUtility**](https://github.com/Cratesmith/RestSharp-for-unity3d/tree/master/RestSharp/Extensions/MonoHttp)
   - Import all three classes into your project, and use the `RestSharp.Contrib` namespace to call `HttpUtility.HtmlDecode (yourHtmlTextToDecode);`
   - [link](https://forum.unity.com/threads/encode-decode-html-tag-in-unity.96484/)

- [**Json for Unity**](https://assetstore.unity.com/packages/tools/input-management/json-net-for-unity-11347)
  - Ensuite utiliser using `RestSharp.Contrib; HttpUtility; Newtonsoft.Json;`

### 2) Utiliser la librairie d'appels web de .Net 3.2 
```
var httpWebRequest = (HttpWebRequest)WebRequest.Create("https://tbdc4269af235b094aa17ea0.servicebus.windows.net/trajectory/messages");
httpWebRequest.Headers.Add("Authorization", "SharedAccessSignature sr=https%3a%2f%2ftbdc4269af235b094aa17ea0.servicebus.windows.net%2f&sig=C%2fs5dntjn10csK1hKoCP9fVGC0MwFvyqd0RaAQaGI0Q%3d&se=1516977535&skn=Send");
httpWebRequest.ContentType = "application/json";
httpWebRequest.Method = "POST";

using (var streamWriter = new StreamWriter(httpWebRequest.GetRequestStream()))
{
    string json = "{\"user\":\"test\"," +
                  "\"password\":\"bla\"}";

    streamWriter.Write(json);
    streamWriter.Flush();
    streamWriter.Close();
}

var httpResponse = (HttpWebResponse)httpWebRequest.GetResponse();
using (var streamReader = new StreamReader(httpResponse.GetResponseStream()))
{
    var result = streamReader.ReadToEnd();
}
```

- Nécessite aussi d'autoriser tous les certificats
- La librairie d'appels web de Unity devrait aussi fonctioner

## Testé 

- .Net 4.6 est disponible sous Unity en version expérimentale
   - Le changement de version de .Net n'a pas l'air d'être pris en compte, il semble qu'il faille supprimer la ligne  
  `Ligne 21 : <LangVersion Condition=" '$(VisualStudioVersion)' != '10.0' ">4</LangVersion>` dans le `.csproject`
   - Fait planter le débugger de Visual Studio Unity au démarrage du jeu : [link](https://issuetracker.unity3d.com/issues/unity-crashes-when-debugging-with-vs2017-when-using-net-4-dot-6), [link2](https://forum.unity.com/threads/crash-during-debugging-net-4-6.476431/)
   - Using System.Net.Http not working and referencing the dll does not work : [link1](https://forum.unity.com/threads/httpclient.460748/), [link2](https://stackoverflow.com/questions/9611316/system-net-http-missing-from-namespace-using-net-4-5)
   - Copying `System.Net.Http` dll from `C:\Program Files\Unity\Editor\Data\MonoBleedingEdge\lib\mono\gac` to `assets/pluggi`n not working either

- Un utilisant Unity, une requête ne peut pas être faite dans un thread car le  GameObject dispacher ne peux pas être créer dans un thread
