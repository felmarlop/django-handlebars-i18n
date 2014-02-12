django-handlebars-i18n
======================

Tools for using django translations in handlebars templates, and making it easier to use translations.

To install:

    pip install -e git://github.com/vegitron/django-handlebars-i18n#egg=Django-Handlebars-I18N
    
To use, you need to do the following:

* add 'handlebars_i18n', to your settings.py file's INSTALLED_APPLICATIONS:
* add  url(r'^t18n/', include('handlebars_i18n.urls')), to your project's urls.py file
* Add the following to the page you want to use django translations in handlebars:


    {% load handlebars_i18n %}
    
    {% handlebars_i18n_scripts "app_name" %}

That will load 2 javascript files onto your page.  One can be compressed the other is (currently) dynamically generated.  To load them separately, you can use

    {% hb_i18_script %}
    {% i18n_catalog "app_name" %}
    
The script is compressable, the catalog is not.

Then in your handlebars templates you can start using the {{ trans }} tag.  

    {{ trans "single value with %(name)s" }}
    
    {{ trans "There is one item" "There are %(count_variable) items" count_variable }}
    
The strings are given the handlebars context, so %(variable)s values will be interpolated.    
