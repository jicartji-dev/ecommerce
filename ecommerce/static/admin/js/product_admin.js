(function ($) {
    $(document).ready(function () {

        $('#id_category').change(function () {
            const categoryId = $(this).val();
            const subSelect = $('#id_subcategory');

            subSelect.empty();
            subSelect.append('<option value="">---------</option>');

            if (!categoryId) return;

            $.ajax({
                url: '/admin/load-subcategories/',
                data: {
                    category: categoryId
                },
                success: function (data) {
                    data.forEach(function (item) {
                        subSelect.append(
                            `<option value="${item.id}">${item.name}</option>`
                        );
                    });
                }
            });
        });

    });
})(django.jQuery);
