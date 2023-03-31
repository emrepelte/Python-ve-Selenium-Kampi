PyTest'te kullanılan yaygın decoratorlar:

@pytest.mark
PyTest'te kullanılan en yaygın decorator olan @pytest.mark sayesinde testlerinizi etiketleyebilir ve filtreleyebilirsiniz.

@pytest.fixture
@pytest.fixture decorator'ı, testlerde kullanılacak ortak kaynaklar için kullanılır. Özellikle, testlerin başlamadan önce 
belirli bir durumu başlatma ve testlerin tamamlanmasından sonra temizleme işlemleri için kullanılır.

@pytest.parametrize
@pytest.parametrize decorator'ı, farklı parametre kombinasyonlarıyla bir testi çalıştırmak istediğinizde kullanılır. 
Bu, testlerinizin farklı girdi değerleriyle nasıl davrandığını kontrol etmek için kullanışlıdır.
