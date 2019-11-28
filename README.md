# Fetscrape

The script helps you scraping users from FetLife, the most popular BDSM-related social network. Basically, it crawls the users of a certain area and export them to a .csv file.


## Project Status

Currently (November 2019) the script works like a charm. I will not maintain the code over time though. Should John change the HTML structure, the script will need to be updated accordingly. Feel free step in as a maintainer.


## Description

Before running the script you will need to insert your FL credentials (username and password) under 'login_data'. Please, do not change the other parameters.
By default, when running the script, the list of the users located in Berlin, Germany will be captured:

```bash
https://fetlife.com/p/germany/berlin/kinksters?page=1
```

Of course, it is possible to change the targeted area. All you have to do is:
1) Browse the desired location in FetLife
2) Copy the URL of that location 
3) Replace the URL in 'r2'

Pay attention to the paging or it will return the results of the first page only!

For each user you are going to store in the .csv file the following information:

- User ID (for later reference; also useful if you are planning to load the users in a target system and would like to prevent the creation of duplicates)
- Username 
- Age / Gender (for simplicity I did not split them: I know, I am lazy, but you can still filter the results using "contains")
- Role
- Location
- Extras (number of pictures / videos / posts)
- Link to the profile page


## Final comments
Please keep in mind I am new to Python and I do not work as a programmer: I am pretty sure it would have been possible to write a better code... But, hey, in the end mine works too and that's what really counts! :-D
If you found this script useful, don't forget to show some love to @Objectivist on FetLife :-D

## License

[MIT](https://choosealicense.com/licenses/mit/)