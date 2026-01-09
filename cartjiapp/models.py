from email.mime import image
from pickle import TRUE
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from cloudinary.models import CloudinaryField


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    image = CloudinaryField('category-image', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Category.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name



class SubCategory(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='subcategories'
    )
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while SubCategory.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.category.name} → {self.name}"

class Size(models.Model):
    name = models.CharField(max_length=20)  # S, M, L, XL

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=7)  # #000000

    def __str__(self):
        return self.name + self.code

class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )
    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.CASCADE,
        related_name='products',
        null=True,
        blank=True
    )

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    sizes = models.ManyToManyField(Size, blank=True)
    
    original_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="MRP",
        null=True,

    )
    discount_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="Leave blank if no discount"
    )


    description = models.TextField()
    views = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Product.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    # ✅ FINAL PRICE LOGIC
    @property
    def selling_price(self):
        return self.discount_price if self.discount_price else self.original_price

    # ✅ DISCOUNT %
    @property
    def discount_percentage(self):
        if self.discount_price:
            return int(
                ((self.original_price - self.discount_price)
                 / self.original_price) * 100
            )
        return 0

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])

    def __str__(self):
        return self.name




class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images'
    )
    # image = models.ImageField(upload_to='products/')
    image = CloudinaryField('image')
    color = models.ForeignKey(
        Color,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.product.name} - {self.color.name if self.color else 'No Color'}"


class ProductVariant(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='variants'
    )
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name} - {self.size} - {self.color}"



class Review(models.Model):
    image = models.ImageField(upload_to="reviews/")
    caption = models.CharField(
        max_length=200,
        blank=True,
        help_text="Optional short caption (e.g. Loved the quality!)"
    )
    rating = models.PositiveIntegerField(default=5)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review {self.id}"
