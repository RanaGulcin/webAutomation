Specification Heading
=====================
Created by rana.cakir on 21.03.2025

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.

//IKWS-FT-001-1
Sistemde kayitli kullanicinin login olma islemi
-----------------------------------------------
*Telefon "5316869882" , sifre "Test1234" ile basarili login islemi

//IKWS-FT-001-2
Bos inputlarla basarisiz login olma islemi
-----------------------------------------------
* Telefon , sifre bilgisi girilmeden login islemi

//IKWS-FT-001-3
Basarisiz login olma islemi (hatali tel no)
-----------------------------------------------
* Telefon "5055000000" , sifre "Test1234" ile basarisiz login islemi

//IKWS-FT-001-4
Basarisiz login olma islemi (hatali sifre formati)
--------------
* Telefon "5316869882" , sifre "test1234" ile basarisiz login islemi

//IKWS-FT-001-5
Basarisiz login olma islemi (hatali tel no ve yanlis sifre formati)
--------------
* Telefon "5055000000" , sifre "test1234" ile basarisiz login islemi

//IKWS-FT-002-1
Sistemde kayitli olmayan kullanicinin login olma islemi
-----------------------------------------------
* Telefon "5316869883" , sifre "Test1234" ile basarisiz login islemi