from django import forms
from cartjiapp.models import Color, Coupon, Order, Product, ProductImage, Size, Category, SubCategory

# begin

class CJColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = ["name", "code"]


class CJSizeForm(forms.ModelForm):
    class Meta:
        model = Size
        fields = ["name"]


class CJCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "slug", "image"]


class CJSubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ["category", "name", "slug"]


# product

class CJProductCreateForm(forms.ModelForm):
    sizes = forms.ModelMultipleChoiceField(
        queryset=Size.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Product
        fields = [
            "category",
            "subcategory",
            "name",
            "original_price",
            "discount_price",
            "description",
            "is_active",
        ]



class CJProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ["image", "color"]



class CJOrderForm(forms.ModelForm):
    size = forms.ModelChoiceField(
        queryset=Size.objects.all(),
        required=False
    )
    color = forms.ModelChoiceField(
        queryset=Color.objects.all(),
        required=False
    )

    class Meta:
        model = Order
        fields = [
            "order_id",
            "product",
            "price",
            "size",
            "color",
            "customer_name",
            "phone",
            "payment_method",
            "status",
        ]




class CJCouponForm(forms.ModelForm):
    class Meta:
        model = Coupon
        fields = ["code", "discount_percent", "is_active"]