# Communiquer en préservant la confidentialité des informations

## Ressources

* [Gestes professionnels](https://github.com/Aif4thah/Dojo-101)
* [Guide ANSSI](https://cyber.gouv.fr/publications/mecanismes-cryptographiques)
* Dossier Toolbox RF


0. Parmis les algorithems qui ne devraient plus être utilisés: 
- AES 128 avec ECB : non sécurisé car il ne fournit pas d’aléa et expose les motifs dans le texte chiffré.
- 3DES : obsolète et vulnérable aux attaques, en particulier avec la progression des capacités de calcul.
- SHA1 : obsolète et vulnérable aux attaques de collision.
- MD5 : obsolète et vulnérable aux attaques de collision.
- RSA avec PKCS1 : moins sécurisés que OAEP.

1. Grâce à un script, générer une clé de chiffrement AES256 ainsi que les IV avec le destinataire. Partagez là avec votre destinataire en essayant de préserver sa confidentialité.

Voir Script clé de chiffrement AES256

2. Comment générer une clé de chiffrement de manière sure ? Quel est le risque si les IV sont toujours les mêmes ?

En utilisant des bibliothèques de cryptographiques robustes qui s'appuient sur des générateurs de nombres aléatoires cryptographiquement sécurisés ("cryptography").
Utilisation de IV statiques présente plusieurs risques tel que les attaques par texte claire connu, manque d'aléa ou encore attaques par réutilisation.

3. Chiffrer un message et l’envoyer.

A l'aide du script en annexe.

![Alt text](https://github.com/Slimnad/MESP_CRYPTO_/blob/main/cryptage_%26_dechiffrement_message.png)

4. Recevoir et déchiffrer le message

![Alt text](https://github.com/Slimnad/MESP_CRYPTO_/blob/main/resultat_dechiffrement.png)

5. Comment pourrait-on s'assurer de l'intégrité du message et de l'authenticité du destinataire ?
En effectuant un chiffrement clé public / privée pour l'authenticité du destinataire et pour vérifier l'intégrité, le message peut être accompagné d'un haché ou d'une signature numérique.

7. Le message suivant a été intercepté: "prggr grpuavdhr f'nccryyr yr puvsserzrag qr prnfre, vy a'rfg cyhf hgvyvft nhwbheq'uhv, pne crh ftphevft", il semble vulnérable à une attaque en fréquences ou une attaque par force brute. Déchiffrez-le !

Le message utilise un chiffrement de type ROT13, une méthode de chiffrement par substitution dans laquelle chaque lettre est remplacée par la lettre située 13 positions après dans l'alphabet. 

Cela nous donne : "Cette technique s'appelle le chiffrement de Céasar, il n'est plus utile d'utiliser aujourd'hui, car peu sécurisé."

8. Nous suspectons qu'un adversaire a implémenté une backdoor dans notre logiciel de messagerie sécurisé, pourtant nous utilisons AES-CBC, trouver le problème et proposer une solution.

Le problème est l'utilisation du même IV qui produit des blocs chiffrés identiques ("\xde@=\x1ed\xc0Qe\x0fK=\x1c\xb3$\xd9\xcb") ainsi en solution l'utilisation d'un générateur aléatoire d'IV nous permet d'éviter ce genre de vulnérabilité.

9. Nous avons intercepté le message suivant: b'\xd72U\xc03.\xda\x99Q\xb5\x020\xc4\xb8\x16\xc6\xfa-\xb9U+\xda\\\x126L\xf3~\xbd8\x12q\x02?\x80\xeaVI\xa9\xe1'.

La première partie de la Clé de 16 octets est: b'12345678bien' 

Quel était le message transmis ?

Le message transmis est "DES n'est plus sur de nors jours!"


