# SQLite Music

## Questions

2.1. Because the key for ArtistId comes from the artist table; it is no good for uniquely identifying
     albums in the Album table.

2.2. Because there is only one artist for any given album, the album's artist can be uniquely identified.
     This is not true in reverse. For any given artist there can be multiple albums, and as such, you can't
     identify an album solely by knowing the artist.

2.3. Using integers is more orderly. It is easier to sort and increment integers than it is to sort and increment the complex strings
     that email addresses can be. It helps to avoid unneccesary hassle.

2.4. SELECT SUM(total) FROM Invoice WHERE InvoiceDate BETWEEN "2010-01-01 00:00:00" AND "2010-12-31 23:59:59";

2.5. SELECT Name FROM Track WHERE TrackId IN (SELECT TrackId FROM InvoiceLine WHERE InvoiceId IN (SELECT InvoiceId FROM Invoice WHERE CustomerId = 50));

2.6. Since the same composers appear multiple times because multiple songs come from an album, a simple solution would be to move the composers column to
     the album table. This way, any given composer (or group of composers) would only have to appear once per body of work, which is more efficient.

## Debrief

a. https://stackoverflow.com/questions/13779338/use-results-from-one-sql-query-in-another-where-statement-subquery

b. 45 minutes
