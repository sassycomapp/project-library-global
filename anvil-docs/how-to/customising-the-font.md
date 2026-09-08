---
title: "Customising your app's font"
url: "/docs/how-to/customising-the-font"
---


# [Customising your app’s font with Google Fonts](#customising-your-apps-font-with-google-fonts)

This is a quick guide to using Google Fonts to customise your app. If you want to change the default font of your app, you’ll need to make minimal modifications to your app’s CSS file. Either way, no prior CSS knowledge is required.

## [Finding your font](#finding-your-font)

[Google Fonts](https://fonts.google.com/) has over 1000 different free fonts to choose from. To get started, navigate to [fonts.google.com](https://fonts.google.com/) and find your perfect font. Click on your chosen font and you’ll see a screen showing all of the available styles for that font. Click “+ Select this style” next to each style you want to be available to your app. A sidebar will appear giving you the appropriate code for importing the chosen font styles into your app.

You can even add multiple font families in one go. Just keep searching for more fonts, select the styles you want, and the newly selected fonts will be added to the code in the sidebar.

## [Importing the font to your app](#importing-the-font-to-your-app)

In the Google Fonts sidebar, `<link>` should be preselected. Copy the HTML code that appears below this, and paste it into your Anvil app’s [Native Libraries](/docs/client/customisation/javascript#using-native-javascript-libraries).

Your code should look something like this:

```html
<link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600&display=swap" rel="stylesheet">
```

## [Changing the font of a component](#changing-the-font-of-a-component)

Once you’ve imported your new font into your app, you can apply this font directly to your Anvil components from the App Editor. Just use the new font as the `font` property of the component.

## [Changing the default font](#changing-the-default-font)

To change the default font of your app, click on “Assets” in the App Browser and select `theme.css` from the dropdown menu. Find the “Typography” section of `theme.css`. Without any modifications, Anvil apps default to Roboto font. The fonts listed after Roboto are what the browser will default to if it cannot display the previously listed font. You can add your new font before Roboto or replace it and the other fonts all together.

```css
/* Typography */
body {
  /*added Montserrat as default*/
  font-family: Montserrat, Roboto, Noto, Arial, sans-serif;
  font-size: 14px;
  line-height: 1.4286;
  background-color: #fafafa;
}
```
