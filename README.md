<img align="right" width="120" alt="rmotr.com" src="https://user-images.githubusercontent.com/7065401/45454218-80bee800-b6b9-11e8-97bb-bb5e7675f440.png">

# Coinmarketcap Django Forms

In our [previous class](https://github.com/rmotr-curriculum/wdc-class-1-coinmarketcap-clone) we've added some features to the [https://coinmarketcap.com/](https://coinmarketcap.com/) clone that we've been implementing. Today we will keep augmenting it with some more Django functionalities. 🙌

We want you to learn how to make usage of all the built-in Forms features that come with Django. This will simplify a lot the work related to validation, rendering forms, and much more.

The main idea is to stop struggling with HTML code and views with tons of logic inside.


## 1) Working with Django Forms

The first approach to our final solution will be focused on implementing the `Create Cryptocurrency` form using [Django Forms](https://docs.djangoproject.com/en/2.1/topics/forms/#building-a-form-in-django).

Everything should look similar to the form that we had in our previous project, but this time the rendering and validation will be in charged of Django instead of our own.

We'll keep using [Bootstrap](https://getbootstrap.com/) to make the form prettier in terms of styles.

<img width="868" alt="screen shot 2019-01-01 at 16 49 23" src="https://user-images.githubusercontent.com/2788551/50575892-43f03b80-0de5-11e9-9846-73891049bf35.png">

## 2) Working with Django ModelForms

One step forward is to use [Django ModelForms](https://docs.djangoproject.com/en/2.1/topics/forms/modelforms/). This kind of forms are linked to a model (in our case, the `Cryptocurrency` model) and we can specify which of the model's fields must be part of the form, instead of defining all the fields one by one.

As each form field is taken from the model, all the validation will be based on the type of field.

## 3) Forms Validations and Widgets

In this final step we'll learn how to change the default widget for certain form field, and also how to validate anything we need at field level or even after every field was correctly validated.

That's all! 🎉 We just did a third iteration to the Coinmarketcap clone, adding some more advanced functionalities of the Django framework.
