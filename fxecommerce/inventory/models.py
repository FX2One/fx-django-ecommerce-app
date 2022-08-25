# https://simpleisbetterthancomplex.com/tips/2016/10/17/django-tip-18-translations.html
# usage of ugettext_lazy
from django.utils.translation import gettext_lazy as _
from django.db import models


class Category(models.Model):
    category_id = models.AutoField(
        verbose_name=_('Category ID'),
        db_column='CategoryID',
        primary_key=True
    )
    category_name = models.CharField(
        verbose_name=_('Category name'),
        db_column='CategoryName',
        max_length=100,
        null=False,
        blank=False,
        db_index=True,
        help_text=_("format: required. Max_length: 100")
    )
    description = models.TextField(
        verbose_name=_('Description'),
        db_column='Description',
        max_length=150,
        blank=False,
        help_text=_("format: required. Max_length: 150")
    )
    image = models.ImageField(
        verbose_name=_('Image'),
        db_column='Image',
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'category'
        verbose_name_plural = _("Product categories")

    def __str__(self):
        return self.category_name


class Supplier(models.Model):
    supplier_id = models.AutoField(
        verbose_name=_('Supplier ID'),
        db_column='SupplierID',
        primary_key=True
    )
    company_name = models.CharField(
        verbose_name=_('Company name'),
        db_column='CompanyName',
        max_length=40,
        blank=False,
        null=False
    )
    contact_name = models.CharField(
        verbose_name=_('Contact name'),
        db_column='ContactName',
        max_length=30,
        blank=False,
        null=False
    )
    contact_title = models.CharField(
        verbose_name=_('Contact title'),
        db_column='ContactTitle',
        max_length=30,
        blank=False,
        null=False
    )
    address = models.CharField(
        verbose_name=_('Address'),
        db_column='Address',
        max_length=60,
        blank=False,
        null=False
    )
    city = models.CharField(
        verbose_name=_('City'),
        db_column='City',
        max_length=15,
        blank=False,
        null=False
    )
    region = models.CharField(
        verbose_name=_('Region'),
        db_column='Region',
        max_length=15,
        blank=False,
        null=False
    )
    postal_code = models.CharField(
        verbose_name=_('Postal code'),
        db_column='PostalCode',
        max_length=10,
        blank=False,
        null=False
    )
    country = models.CharField(
        verbose_name=_('Country'),
        db_column='Country',
        max_length=15,
        blank=False,
        null=False
    )
    phone = models.CharField(
        verbose_name=_('Phone'),
        db_column='Phone',
        max_length=24,
        blank=False,
        null=False
    )
    fax = models.CharField(
        verbose_name=_('Fax'),
        db_column='Fax',
        max_length=24,
        blank=True,
        null=True
    )
    homepage = models.TextField(
        verbose_name=_('HomePage'),
        db_column='HomePage',
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'supplier'
        verbose_name_plural = _("Suppliers")

    def __str__(self):
        return self.company_name



class Product(models.Model):
    product_id = models.AutoField(
        verbose_name=_('Product ID'),
        db_column='ProductID',
        primary_key=True
    )
    product_name = models.CharField(
        verbose_name=_('Product name'),
        db_column='ProductName',
        max_length=100,
        null=False,
        blank=False,
        db_index=True,
        help_text=_("format: required. max_length: 100")
    )
    supplier_id = models.ForeignKey(
        Supplier,
        db_column='SupplierID',
        blank=True,
        null=True,
        db_index=True,
        on_delete=models.CASCADE,
    )
    category_id = models.ForeignKey(
        Category,
        db_column='CategoryID',
        blank=True,
        null=True,
        db_index=True,
        on_delete=models.CASCADE
    )
    quantity_per_unit = models.CharField(
        verbose_name=_('Quantity per Unit'),
        db_column='QuantityPerUnit',
        max_length=20,
        blank=False,
        null=False
    )
    unit_price = models.DecimalField(
        verbose_name=_('Unit price'),
        db_column='UnitPrice',
        blank=True,
        null=True,
        max_digits=19,
        decimal_places=4
    )
    units_in_stock = models.SmallIntegerField(
        verbose_name=_('Units in Stock'),
        db_column='UnitsInStock',
        blank=True,
        null=True
    )
    units_on_order = models.SmallIntegerField(
        verbose_name=_('Units on Order'),
        db_column='UnitsOnOrder',
        blank=True,
        null=True
    )
    reorder_level = models.SmallIntegerField(
        verbose_name=_('Reorder level'),
        db_column='ReorderLevel',
        blank=True,
        null=True
    )
    discontinued = models.BooleanField(
        verbose_name=_('Discontinued'),
        db_column='Discontinued',
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.product_name

    class Meta:
        db_table = 'product'
        verbose_name_plural = _("Products")


class Order(models.Model):
    order_id = models.AutoField(
        verbose_name=_('Order ID'),
        db_column='OrderID',
        primary_key=True
    )
    customer = models.ForeignKey(
        Customer,
        db_column='CustomerID',
        blank=True,
        null=True,
        db_index=True,
        on_delete=models.CASCADE,
    )
    employee = models.ForeignKey(
        Employee, #create
        db_column='EmployeeID',
        blank=True,
        null=True,
        db_index=True,
        on_delete=models.CASCADE,
    )
    order_date = models.DateField(
        verbose_name=_('Order date'),
        db_column='OrderDate',
        blank=True,
        null=True,
        db_index=True
    )
    required_date = models.DateField(
        verbose_name=_('Required_date'),
        db_column='RequiredDate',
        blank=True,
        null=True
    )
    shipped_date = models.DateField(
        verbose_name=_('Shipped date'),
        db_column='ShippedDate',
        blank=True,
        null=True,
        db_index=True
    )
    ship_via = models.ForeignKey(
        Shipper, #create
        db_column='ShipVia',
        blank=True,
        null=True,
        db_index=True,
        on_delete=models.CASCADE,
    )
    freight = models.DecimalField(
        verbose_name=_('Freight'),
        db_column='Freight',
        blank=True,
        null=True,
        max_digits=19,
        decimal_places=4
    )
    ship_name = models.CharField(
        verbose_name=_('Ship name'),
        db_column='ShipName',
        max_length=40,
        blank=False,
        null=False,
    )
    ship_address = models.CharField(
        verbose_name=_('Ship address'),
        db_column='ShipAddress',
        max_length=60,
        blank=False,
        null=False
    )
    ship_city = models.CharField(
        verbose_name=_('Ship city'),
        db_column='ShipCity',
        max_length=15,
        blank=False,
        null=False
    )
    ship_region = models.CharField(
        verbose_name=_('Ship region'),
        db_column='ShipRegion',
        max_length=15,
        blank=True,
        null=True
    )
    ship_postal_code = models.CharField(
        verbose_name=_('Ship postal code'),
        db_column='ShipPostalCode',
        max_length=10,
        blank=False,
        null=False,
        db_index=True
    )
    ship_country = models.CharField(
        verbose_name=_('Shipped country'),
        db_column='ShipCountry',
        max_length=15,
        blank=False,
        null=False
    )
    order_details = models.ManyToManyField(
        Product,
        verbose_name=_('Products'),
        blank=True,
        through='OrderDetails'
    )

    def __str__(self):
        return self.order_id

    class Meta:
        db_table = 'order'
        verbose_name_plural = _("Orders")


class Customer(models.Model):
    customer_id = models.CharField(
        verbose_name=_('Customer ID'),
        db_column='CustomerID',
        primary_key=True,
        max_length=5
    )
    company_name = models.CharField(
        verbose_name=_('Company name'),
        db_column='CompanyName',
        max_length=40
    )
    contact_name = models.CharField(
        verbose_name=_('Contact name'),
        db_column='ContactName',
        max_length=30,
        blank=True,
        null=True
    )
    contact_title = models.CharField(
        verbose_name=_('Contact title'),
        db_column='ContactTitle',
        max_length=30,
        blank=True,
        null=True
    )
    address = models.CharField(
        verbose_name=_('Address'),
        db_column='Address',
        max_length=60,
        blank=True,
        null=True
    )
    city = models.CharField(
        verbose_name=_('City'),
        db_column='City',
        max_length=15,
        blank=True,
        null=True
    )
    region = models.CharField(
        verbose_name=_('Region'),
        db_column='Region',
        max_length=15,
        blank=True,
        null=True
    )
    postal_code = models.CharField(
        verbose_name=_('Postal code'),
        db_column='PostalCode',
        max_length=10,
        blank=True,
        null=True
    )
    country = models.CharField(
        verbose_name=_('Country'),
        db_column='Country',
        max_length=15,
        blank=True,
        null=True
    )
    phone = models.CharField(
        verbose_name=_('Phone'),
        db_column='Phone',
        max_length=24,
        blank=True,
        null=True
    )
    fax = models.CharField(
        verbose_name=_('Fax'),
        db_column='Fax',
        max_length=24,
        blank=True,
        null=True
    )
    customer_customer_demo = models.ManyToManyField(
        CustomerDemographics,
        verbose_name=_('Customer customer demo'),
        db_table='CustomerCustomerDemo',
        blank=True,
    )

    class Meta:
        db_table = 'customer'
        verbose_name_plural = _("Customers")

    def __str__(self):
        return self.company_name

class CustomerDemographics(models.Model):
    customer_type_id = models.CharField(
        varbose_name=_('Customer typeID'),
        db_column='CustomerTypeID',
        primary_key=True,
        max_length=5
    )
    customer_desc = models.TextField(
        verbose_name=_('Customer description'),
        db_column='CustomerDesc',
        blank=True,
        null=True
    )
    class Meta:
        db_table = 'customerdemographics'


class Shipper(models.Model):
    shipper_id = models.AutoField(
        verbose_name=_('Shipper ID'),
        db_column='ShipperID',
        primary_key=True
    )
    company_name = models.CharField(
        _('Company name'),
        db_column='CompanyName',
        max_length=40
    )
    phone = models.CharField(
        _('Phone'),
        db_column='Phone',
        max_length=24,
        blank=False,
        null=False
    )

    class Meta:
        db_table = 'shipper'
        verbose_name_plural = _('Shippers')

'''class Employee:
    pass'''