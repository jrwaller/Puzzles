How this project came to be:

This project started out as way to get guitar tabs more easily. 
Many of the songs I needed tabs for were being blocked in the US. 
They could be accessed using the Hola Unblocker extension, but this was tedious every time I wanted a guitar tab.

I used Chrome's inspect element tool to view the HTML of the guitar pro tab pages and found that Ultimate Guitar provides the Tab-ID in a hidden field. Using the tab ID and the default style of Ultimate Guitar's tab download URLs, I was able to create download links for any guitar tab, even if they were blocked in the US. I decided that I could write this functionality into a program so I'd never have to spend a great deal of time searching for alternate tabs. 

The first iteration of this project was a Python script that used Selenium web drivers and URLLib libraries to fetch a guitar tab when I input a URL to a guitar pro tab page.
This proved to also be tedious since it had to launch an instance of Firefox every single time, pasting URL links into the script directly was annoying, and I had to deal with downloading issues such as having to click "Save to File" every single time. 
I experimented with PhantomJS as an alternative, but it was difficult to download files using it. Rather than call it quits here, I decided that the best way to do this would be to incorporate it into a Chrome extension.

I used Google's tutorials for the Manifest, and I taught myself enough JS to interact with the elements on the page. After quite a bit of testing, I managed to get a working prototype.

This represents the current product in unpackaged form. 

Usage: Visit a Guitar Pro or Power Tab on Ultimate Guitar after loading the extension, and click the Guitar Symbol in the Extensions bar within Chrome. 

The program automatically checks if the page is valid, extracts the ID from the hidden field, and crafts the download links, which it conveniently opens and downloads for you. 
