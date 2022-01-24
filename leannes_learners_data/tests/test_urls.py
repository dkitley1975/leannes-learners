from django.test import SimpleTestCase
from django.urls import reverse, resolve
from leannes_learners_data.views import AboutUsPage, BlogDetail, BlogPage, ContactUsPage, ContactSuccessView, PassPlusPage, PricesPage, TermsPage, Testimonials


class TestUrls(SimpleTestCase):
    """ Test the URLS """


    def test_about_Us_url(self):
        """ Test the About Us URL """
        url = reverse('about_us')
        self.assertEquals(resolve(url).func.view_class, AboutUsPage)

    def test_Home_Page_url(self):
        """ Test the Home Page URL """
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class, Testimonials)

    def test_Blog_Page_url(self):
        """ Test the Blog Page URL """
        url = reverse('blogs')
        self.assertEquals(resolve(url).func.view_class, BlogPage)
    
    def test_Contact_Us_url(self):
        """ Test the Contact Us Page URL """
        url = reverse('contact_us')
        self.assertEquals(resolve(url).func.view_class, ContactUsPage)

    def test_Pass_Plus_Page_url(self):
        """ Test the Pass Plus Page URL """
        url = reverse('pass_plus')
        self.assertEquals(resolve(url).func.view_class, PassPlusPage)

    def test_Prices_Page_url(self):
        """ Test the Prices Page URL """
        url = reverse('prices')
        self.assertEquals(resolve(url).func.view_class, PricesPage)

    def test_Contact_Success_Page_url(self):
        """ Test the Successful Contact Page URL """
        url = reverse('success')
        self.assertEquals(resolve(url).func.view_class, ContactSuccessView)

    def test_Ts_and_Cs_Page_url(self):
        """ Test the Terms and Conditions Page URL """
        url = reverse('terms_and_conditions')
        self.assertEquals(resolve(url).func.view_class, TermsPage)

    def test_Blog_Detail_Page_url(self):
        """ Test the Blog Post Detail Page URL """
        url = reverse('blog_post_view', args=['My-Great-First-Blog-slug'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, BlogDetail)
        