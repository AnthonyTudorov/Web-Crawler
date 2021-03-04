<h2>Web Crawler</h2>
Crawls Wikipedia pages by starting from a list of seed urls and searching for terms given in related terms.
A link is written to results and the page is saved if it contains at least two of the related terms.
The web crawler works until 500 links are returned.
<br/><br/>
There are two ways to generate an index: Frequency based or position based.
Position based is more useful with the trade-off that it is larger and can be used to derive a frequency based index.
The indexing requires that the pages directory be present and filled with only html files.
Indexes are saved in text format to either "frequency index.txt" or "position index.txt".
The terms used as the keys in the indexes are also saved to "terms.txt".
The total unique terms is returned when the indexer finishes execution.
