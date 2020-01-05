# Fetscrape

This is a basic script that helps you scraping users from FetLife, the most popular BDSM-related social network. Basically, it crawls the users of a certain area and export them to a .csv file.


## Status

Currently (November 2019) the script works like a charm. I will not maintain the code over time though. Should John change the HTML structure, the script will need to be updated accordingly. Feel free step in as a maintainer.


## Usage / Description

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

For each user you are going to store in the .csv file some basic information:

- User ID (for later reference; also useful to load profile information into a target system and prevent the creation of duplicates)
- Username 
- Age / Gender (I did not split them: I know, I am lazy, but you can still filter the results using "contains")
- Role
- Location
- Extras (number of pictures / videos / posts)
- Link to the profile page

## Final comments
If you found this script useful, don't forget to show some love to [@Objectivist](https://fetlife.com/users/1296385) on FetLife :-D

