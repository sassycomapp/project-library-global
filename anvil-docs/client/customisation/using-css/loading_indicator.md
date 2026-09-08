---
title: "Customising the Loading Indicator"
url: "/docs/client/customisation/using-css/loading_indicator"
---


# [Loading Indicator](#loading-indicator)

A loading indicator is displayed when your app is retrieving data. This stops users from being able to interact with your app while the server returns data.

## [Customising the indicator](#customising-the-indicator)

The default indicator that comes with Anvil apps is a spinner [SVG](https://developer.mozilla.org/en-US/docs/Web/SVG). By default, the colour of the indicator will change to match your app’s selected [colour scheme](https://anvil.works/docs/client/customisation/colour-schemes#changing-the-colour-scheme).

If you want to customise the spinner, you can do so from CSS.

### Changing the colour with CSS

You can change the colour of the indicator using CSS.

This is an advanced feature. You don’t need to write CSS to use Anvil. If you’re new to styling Anvil apps with CSS, [check out our guide here](https://anvil.works/articles/using-css).

In your app’s code, open the [theme.css](https://anvil.works/articles/using-css#writing-css-in-the-stylesheet) file in the [App Browser](https://anvil.works/docs/editor#app-browser) and use the `.anvil-spinner` [class](https://developer.mozilla.org/en-US/docs/Web/CSS/Class_selectors) to customise the colour of your indicator.

```CSS
.anvil-spinner {
  color: lightblue;
}
```

This lets you use any [colour value](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value) available in CSS.

### Changing the svg

You can change the SVG your app uses as a indicator using CSS.

This is an advanced feature. You don’t need to write CSS to use Anvil. If you’re new to styling Anvil apps with CSS, [check out our guide here](https://anvil.works/articles/using-css).

Using the `.anvil-spinner` [class](https://developer.mozilla.org/en-US/docs/Web/CSS/Class_selectors), you can use [`background-image: url()`](https://developer.mozilla.org/en-US/docs/Web/CSS/background-image) to replace the default spinner with an SVG or image hosted online.

```CSS
.anvil-spinner {
  /* Remove the border-radius of the default Anvil spinner. */  
  border-radius: 0px;

  /* Replace the default spinner SVG */
  background-image: url("https://raw.githubusercontent.com/n3r4zzurr0/svg-spinners/main/svg-smil/blocks-shuffle-3.svg");
}
```

You can use a file from your [app’s assets](https://anvil.works/docs/client/customisation#adding-your-own-asset-files). To do this, start by uploading the SVG, image or gif to your [app’s assets](https://anvil.works/docs/client/customisation#adding-your-own-asset-files). The asset you uploaded will have a path like `_/theme/<asset-folder>/<asset-name>` - here’s an example:

```CSS
.anvil-spinner {
    background-image: url(_/theme/my-new-spinner.gif);
}
```

You may want to remove some of the styling that comes with the default spinner, so here are some common thing’s you’ll want to do:

```CSS
.anvil-spinner {
    /* Replacing the default spinner with a file hosted in the app's assets */
    background-image: url(_/theme/my-new-spinner.gif);

    /* Here's a way to centre the spinner horizontally in your app, if your spinner is a different size */
    width: 400px;
    left: calc(50% - 400px/2);

    /* Here we are removing some of the default styling */ 
    box-shadow: none; 
    background-color: transparent;
}
```

CSS offers a wide range of options to customise your spinner using the numerous [properties](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics#properties) available. If you’re new to styling Anvil apps with CSS, [check out our guide here](https://anvil.works/articles/using-css).
