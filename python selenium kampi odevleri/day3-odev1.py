# Aşağıdaki konuları araştırıp not alarak notlarınızı arkadaşlarınızla bu ödevin yorum kısmında paylaşınız;

# HTML
# HTML Locators
# Selenium'da aksiyonlar (send_keys, click vb..)

HTML (Hypertext Markup Language), web sayfalarını oluşturmak ve düzenlemek için kullanılan bir işaretleme dilidir. HTML, sayfadaki metin, bağlantılar, görseller, tablolar ve diğer öğeleri düzenlemek ve görsel olarak sunmak için kullanılır. HTML'de, etiketler (tags) denilen öğelerle yapılandırılır. Örnek olarak basit bir HTML dosyası:

<html>
<head>
  <title>Örnek Web Sayfası</title>
</head>
<body>
  <h1>Merhaba Dünya!</h1>
  <p>HTML öğreniyorum.</p>
  <a href="https://www.orneksite.com">Buraya tıklayarak örnek bir siteye gidin.</a>
</body>
</html>

Bu örnekte, <html> etiketi, HTML belgesinin başlangıcını ve sonunu belirtir. <head> etiketi, sayfanın başlık gibi meta bilgilerini içerir. <body> etiketi ise sayfanın görünür içeriğini içerir. <h1> ve <p> etiketleri başlık ve paragraf oluştururken, <a> etiketi ise bir bağlantı (link) oluşturur.

# ------------------------------------------------------

HTML locators, bir web sayfasındaki öğeleri (element) tanımlamak ve bulmak için kullanılan yöntemlerdir. Bu öğeler, sayfadaki metin, görseller, bağlantılar vb. olabilir. Otomasyon, test ve web sayfası analizi gibi alanlarda HTML locators kullanılır. Selenium gibi web otomasyon araçlarıyla birlikte, CSS seçicileri (selectors) ve XPath kullanarak öğeleri belirleyebilirsiniz.

Örnek:

Bir sayfadaki tüm başlık etiketlerini (h1) CSS seçicisi kullanarak belirlemek istediğimizi düşünelim:

css
h1

xpath
//h1

# -------------------------------------------------------

Selenium, web tarayıcılarında otomasyon sağlayan bir yazılım çerçevesidir. Selenium WebDriver ile, programlama dilleri (Python, Java vb.) kullanarak tarayıcılar üzerinde işlem gerçekleştirebilirsiniz. Aksiyonlar, Selenium'da belirli elementlerle etkileşime geçmek için kullanılır. İki temel aksiyon türü vardır:
- send_keys: Bu aksiyon, belirtilen öğeye (örneğin bir input alanına) metin gönderir. Kullanıcı gibi yazı yazabilmenizi sağlar.

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.orneksite.com")

input_element = driver.find_element_by_id("input_id")
input_element.send_keys("Selenium ile yazıyoruz")

Selenium ile Firefox tarayıcısını başlatıyoruz ve "https://www.orneksite.com" adresindeki web sayfasını açıyoruz. Ardından, sayfadaki "input_id" ID'sine sahip olan bir input alanını buluyoruz ve bu alana "Selenium ile yazıyoruz" metnini gönderiyoruz.

- click: Bu aksiyon, belirtilen öğeye (örneğin bir düğmeye veya bağlantıya) tıklama işlemi gerçekleştirir.

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.orneksite.com")

button_element = driver.find_element_by_id("button_id")
button_element.click()

Bu örnekte, "https://www.orneksite.com" adresindeki web sayfasını açıyoruz ve sayfadaki "button_id" ID'sine sahip olan bir düğmeyi (button) buluyoruz. Daha sonra, bu düğmeye tıklama işlemi gerçekleştiriyoruz.

Selenium ile yapılan aksiyonlar, kullanıcıların web sayfalarında gerçekleştirdiği işlemleri taklit eder ve bu sayede otomasyon, test ve web sayfası analizi gibi alanlarda kullanılır.