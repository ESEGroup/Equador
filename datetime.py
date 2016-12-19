<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en-US">
<head>
<link rel="icon" href="/cpython/static/hgicon.png" type="image/png" />
<meta name="robots" content="index, nofollow" />
<link rel="stylesheet" href="/cpython/static/style-paper.css" type="text/css" />
<script type="text/javascript" src="/cpython/static/mercurial.js"></script>

<link rel="stylesheet" href="/cpython/highlightcss" type="text/css" />
<title>cpython: 6f89f5eb4422 Lib/datetime.py</title>
</head>
<body>

<div class="container">
<div class="menu">
<div class="logo">
<a href="https://hg.python.org">
<img src="/cpython/static/hglogo.png" alt="back to hg.python.org repositories" /></a>
</div>
<ul>
<li><a href="/cpython/shortlog/3.5">log</a></li>
<li><a href="/cpython/graph/3.5">graph</a></li>
<li><a href="/cpython/tags">tags</a></li>
<li><a href="/cpython/bookmarks">bookmarks</a></li>
<li><a href="/cpython/branches">branches</a></li>
</ul>
<ul>
<li><a href="/cpython/rev/3.5">changeset</a></li>
<li><a href="/cpython/file/3.5/Lib/">browse</a></li>
</ul>
<ul>
<li class="active">file</li>
<li><a href="/cpython/file/tip/Lib/datetime.py">latest</a></li>
<li><a href="/cpython/diff/3.5/Lib/datetime.py">diff</a></li>
<li><a href="/cpython/comparison/3.5/Lib/datetime.py">comparison</a></li>
<li><a href="/cpython/annotate/3.5/Lib/datetime.py">annotate</a></li>
<li><a href="/cpython/log/3.5/Lib/datetime.py">file log</a></li>
<li><a href="/cpython/raw-file/3.5/Lib/datetime.py">raw</a></li>
</ul>
<ul>
<li><a href="/cpython/help">help</a></li>
</ul>
</div>

<div class="main">
<h2 class="breadcrumb"><a href="/">Mercurial</a> &gt; <a href="/cpython">cpython</a> </h2>
<h3>
 view Lib/datetime.py @ 105727:<a href="/cpython/rev/6f89f5eb4422">6f89f5eb4422</a>
 <span class="branchname">3.5</span> 
</h3>

<form class="search" action="/cpython/log">

<p><input name="rev" id="search1" type="text" size="30" /></p>
<div id="hint">Find changesets by keywords (author, files, the commit message), revision
number or hash, or <a href="/cpython/help/revsets">revset expression</a>.</div>
</form>

<div class="description">#29005: clarify terminology in tutorial 'method' discussion.

Patch by Jim Fasarakis-Hilliard.</a> [<a href="http://bugs.python.org/29005" class="issuelink">#29005</a>]</div>

<table id="changesetEntry">
<tr>
 <th class="author">author</th>
 <td class="author">&#82;&#32;&#68;&#97;&#118;&#105;&#100;&#32;&#77;&#117;&#114;&#114;&#97;&#121;&#32;&#60;&#114;&#100;&#109;&#117;&#114;&#114;&#97;&#121;&#64;&#98;&#105;&#116;&#100;&#97;&#110;&#99;&#101;&#46;&#99;&#111;&#109;&#62;</td>
</tr>
<tr>
 <th class="date">date</th>
 <td class="date age">Sun, 18 Dec 2016 14:59:58 -0500</td>
</tr>
<tr>
 <th class="author">parents</th>
 <td class="author"><a href="/cpython/file/6080d720cbf5/Lib/datetime.py">6080d720cbf5</a> </td>
</tr>
<tr>
 <th class="author">children</th>
 <td class="author"><a href="/cpython/file/3f337cce758c/Lib/datetime.py">3f337cce758c</a> </td>
</tr>
</table>

<div class="overflow">
<div class="sourcefirst linewraptoggle">line wrap: <a class="linewraplink" href="javascript:toggleLinewrap()">on</a></div>
<div class="sourcefirst"> line source</div>
<pre class="sourcelines stripes4 wrap">
<span id="l1"><span class="sd">&quot;&quot;&quot;Concrete date/time and related types.</span></span><a href="#l1"></a>
<span id="l2"></span><a href="#l2"></a>
<span id="l3"><span class="sd">See http://www.iana.org/time-zones/repository/tz-link.html for</span></span><a href="#l3"></a>
<span id="l4"><span class="sd">time zone and DST data sources.</span></span><a href="#l4"></a>
<span id="l5"><span class="sd">&quot;&quot;&quot;</span></span><a href="#l5"></a>
<span id="l6"></span><a href="#l6"></a>
<span id="l7"><span class="kn">import</span> <span class="nn">time</span> <span class="kn">as</span> <span class="nn">_time</span></span><a href="#l7"></a>
<span id="l8"><span class="kn">import</span> <span class="nn">math</span> <span class="kn">as</span> <span class="nn">_math</span></span><a href="#l8"></a>
<span id="l9"></span><a href="#l9"></a>
<span id="l10"><span class="k">def</span> <span class="nf">_cmp</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">):</span></span><a href="#l10"></a>
<span id="l11">    <span class="k">return</span> <span class="mi">0</span> <span class="k">if</span> <span class="n">x</span> <span class="o">==</span> <span class="n">y</span> <span class="k">else</span> <span class="mi">1</span> <span class="k">if</span> <span class="n">x</span> <span class="o">&gt;</span> <span class="n">y</span> <span class="k">else</span> <span class="o">-</span><span class="mi">1</span></span><a href="#l11"></a>
<span id="l12"></span><a href="#l12"></a>
<span id="l13"><span class="n">MINYEAR</span> <span class="o">=</span> <span class="mi">1</span></span><a href="#l13"></a>
<span id="l14"><span class="n">MAXYEAR</span> <span class="o">=</span> <span class="mi">9999</span></span><a href="#l14"></a>
<span id="l15"><span class="n">_MAXORDINAL</span> <span class="o">=</span> <span class="mi">3652059</span>  <span class="c"># date.max.toordinal()</span></span><a href="#l15"></a>
<span id="l16"></span><a href="#l16"></a>
<span id="l17"><span class="c"># Utility functions, adapted from Python&#39;s Demo/classes/Dates.py, which</span></span><a href="#l17"></a>
<span id="l18"><span class="c"># also assumes the current Gregorian calendar indefinitely extended in</span></span><a href="#l18"></a>
<span id="l19"><span class="c"># both directions.  Difference:  Dates.py calls January 1 of year 0 day</span></span><a href="#l19"></a>
<span id="l20"><span class="c"># number 1.  The code here calls January 1 of year 1 day number 1.  This is</span></span><a href="#l20"></a>
<span id="l21"><span class="c"># to match the definition of the &quot;proleptic Gregorian&quot; calendar in Dershowitz</span></span><a href="#l21"></a>
<span id="l22"><span class="c"># and Reingold&#39;s &quot;Calendrical Calculations&quot;, where it&#39;s the base calendar</span></span><a href="#l22"></a>
<span id="l23"><span class="c"># for all computations.  See the book for algorithms for converting between</span></span><a href="#l23"></a>
<span id="l24"><span class="c"># proleptic Gregorian ordinals and many other calendar systems.</span></span><a href="#l24"></a>
<span id="l25"></span><a href="#l25"></a>
<span id="l26"><span class="c"># -1 is a placeholder for indexing purposes.</span></span><a href="#l26"></a>
<span id="l27"><span class="n">_DAYS_IN_MONTH</span> <span class="o">=</span> <span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="mi">31</span><span class="p">,</span> <span class="mi">28</span><span class="p">,</span> <span class="mi">31</span><span class="p">,</span> <span class="mi">30</span><span class="p">,</span> <span class="mi">31</span><span class="p">,</span> <span class="mi">30</span><span class="p">,</span> <span class="mi">31</span><span class="p">,</span> <span class="mi">31</span><span class="p">,</span> <span class="mi">30</span><span class="p">,</span> <span class="mi">31</span><span class="p">,</span> <span class="mi">30</span><span class="p">,</span> <span class="mi">31</span><span class="p">]</span></span><a href="#l27"></a>
<span id="l28"></span><a href="#l28"></a>
<span id="l29"><span class="n">_DAYS_BEFORE_MONTH</span> <span class="o">=</span> <span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>  <span class="c"># -1 is a placeholder for indexing purposes.</span></span><a href="#l29"></a>
<span id="l30"><span class="n">dbm</span> <span class="o">=</span> <span class="mi">0</span></span><a href="#l30"></a>
<span id="l31"><span class="k">for</span> <span class="n">dim</span> <span class="ow">in</span> <span class="n">_DAYS_IN_MONTH</span><span class="p">[</span><span class="mi">1</span><span class="p">:]:</span></span><a href="#l31"></a>
<span id="l32">    <span class="n">_DAYS_BEFORE_MONTH</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">dbm</span><span class="p">)</span></span><a href="#l32"></a>
<span id="l33">    <span class="n">dbm</span> <span class="o">+=</span> <span class="n">dim</span></span><a href="#l33"></a>
<span id="l34"><span class="k">del</span> <span class="n">dbm</span><span class="p">,</span> <span class="n">dim</span></span><a href="#l34"></a>
<span id="l35"></span><a href="#l35"></a>
<span id="l36"><span class="k">def</span> <span class="nf">_is_leap</span><span class="p">(</span><span class="n">year</span><span class="p">):</span></span><a href="#l36"></a>
<span id="l37">    <span class="s">&quot;year -&gt; 1 if leap year, else 0.&quot;</span></span><a href="#l37"></a>
<span id="l38">    <span class="k">return</span> <span class="n">year</span> <span class="o">%</span> <span class="mi">4</span> <span class="o">==</span> <span class="mi">0</span> <span class="ow">and</span> <span class="p">(</span><span class="n">year</span> <span class="o">%</span> <span class="mi">100</span> <span class="o">!=</span> <span class="mi">0</span> <span class="ow">or</span> <span class="n">year</span> <span class="o">%</span> <span class="mi">400</span> <span class="o">==</span> <span class="mi">0</span><span class="p">)</span></span><a href="#l38"></a>
<span id="l39"></span><a href="#l39"></a>
<span id="l40"><span class="k">def</span> <span class="nf">_days_before_year</span><span class="p">(</span><span class="n">year</span><span class="p">):</span></span><a href="#l40"></a>
<span id="l41">    <span class="s">&quot;year -&gt; number of days before January 1st of year.&quot;</span></span><a href="#l41"></a>
<span id="l42">    <span class="n">y</span> <span class="o">=</span> <span class="n">year</span> <span class="o">-</span> <span class="mi">1</span></span><a href="#l42"></a>
<span id="l43">    <span class="k">return</span> <span class="n">y</span><span class="o">*</span><span class="mi">365</span> <span class="o">+</span> <span class="n">y</span><span class="o">//</span><span class="mi">4</span> <span class="o">-</span> <span class="n">y</span><span class="o">//</span><span class="mi">100</span> <span class="o">+</span> <span class="n">y</span><span class="o">//</span><span class="mi">400</span></span><a href="#l43"></a>
<span id="l44"></span><a href="#l44"></a>
<span id="l45"><span class="k">def</span> <span class="nf">_days_in_month</span><span class="p">(</span><span class="n">year</span><span class="p">,</span> <span class="n">month</span><span class="p">):</span></span><a href="#l45"></a>
<span id="l46">    <span class="s">&quot;year, month -&gt; number of days in that month in that year.&quot;</span></span><a href="#l46"></a>
<span id="l47">    <span class="k">assert</span> <span class="mi">1</span> <span class="o">&lt;=</span> <span class="n">month</span> <span class="o">&lt;=</span> <span class="mi">12</span><span class="p">,</span> <span class="n">month</span></span><a href="#l47"></a>
<span id="l48">    <span class="k">if</span> <span class="n">month</span> <span class="o">==</span> <span class="mi">2</span> <span class="ow">and</span> <span class="n">_is_leap</span><span class="p">(</span><span class="n">year</span><span class="p">):</span></span><a href="#l48"></a>
<span id="l49">        <span class="k">return</span> <span class="mi">29</span></span><a href="#l49"></a>
<span id="l50">    <span class="k">return</span> <span class="n">_DAYS_IN_MONTH</span><span class="p">[</span><span class="n">month</span><span class="p">]</span></span><a href="#l50"></a>
<span id="l51"></span><a href="#l51"></a>
<span id="l52"><span class="k">def</span> <span class="nf">_days_before_month</span><span class="p">(</span><span class="n">year</span><span class="p">,</span> <span class="n">month</span><span class="p">):</span></span><a href="#l52"></a>
<span id="l53">    <span class="s">&quot;year, month -&gt; number of days in year preceding first day of month.&quot;</span></span><a href="#l53"></a>
<span id="l54">    <span class="k">assert</span> <span class="mi">1</span> <span class="o">&lt;=</span> <span class="n">month</span> <span class="o">&lt;=</span> <span class="mi">12</span><span class="p">,</span> <span class="s">&#39;month must be in 1..12&#39;</span></span><a href="#l54"></a>
<span id="l55">    <span class="k">return</span> <span class="n">_DAYS_BEFORE_MONTH</span><span class="p">[</span><span class="n">month</span><span class="p">]</span> <span class="o">+</span> <span class="p">(</span><span class="n">month</span> <span class="o">&gt;</span> <span class="mi">2</span> <span class="ow">and</span> <span class="n">_is_leap</span><span class="p">(</span><span class="n">year</span><span class="p">))</span></span><a href="#l55"></a>
<span id="l56"></span><a href="#l56"></a>
<span id="l57"><span class="k">def</span> <span class="nf">_ymd2ord</span><span class="p">(</span><span class="n">year</span><span class="p">,</span> <span class="n">month</span><span class="p">,</span> <span class="n">day</span><span class="p">):</span></span><a href="#l57"></a>
<span id="l58">    <span class="s">&quot;year, month, day -&gt; ordinal, considering 01-Jan-0001 as day 1.&quot;</span></span><a href="#l58"></a>
<span id="l59">    <span class="k">assert</span> <span class="mi">1</span> <span class="o">&lt;=</span> <span class="n">month</span> <span class="o">&lt;=</span> <span class="mi">12</span><span class="p">,</span> <span class="s">&#39;month must be in 1..12&#39;</span></span><a href="#l59"></a>
<span id="l60">    <span class="n">dim</span> <span class="o">=</span> <span class="n">_days_in_month</span><span class="p">(</span><span class="n">year</span><span class="p">,</span> <span class="n">month</span><span class="p">)</span></span><a href="#l60"></a>
<span id="l61">    <span class="k">assert</span> <span class="mi">1</span> <span class="o">&lt;=</span> <span class="n">day</span> <span class="o">&lt;=</span> <span class="n">dim</span><span class="p">,</span> <span class="p">(</span><span class="s">&#39;day must be in 1..</span><span class="si">%d</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">dim</span><span class="p">)</span></span><a href="#l61"></a>
<span id="l62">    <span class="k">return</span> <span class="p">(</span><span class="n">_days_before_year</span><span class="p">(</span><span class="n">year</span><span class="p">)</span> <span class="o">+</span></span><a href="#l62"></a>
<span id="l63">            <span class="n">_days_before_month</span><span class="p">(</span><span class="n">year</span><span class="p">,</span> <span class="n">month</span><span class="p">)</span> <span class="o">+</span></span><a href="#l63"></a>
<span id="l64">            <span class="n">day</span><span class="p">)</span></span><a href="#l64"></a>
<span id="l65"></span><a href="#l65"></a>
<span id="l66"><span class="n">_DI400Y</span> <span class="o">=</span> <span class="n">_days_before_year</span><span class="p">(</span><span class="mi">401</span><span class="p">)</span>    <span class="c"># number of days in 400 years</span></span><a href="#l66"></a>
<span id="l67"><span class="n">_DI100Y</span> <span class="o">=</span> <span class="n">_days_before_year</span><span class="p">(</span><span class="mi">101</span><span class="p">)</span>    <span class="c">#    &quot;    &quot;   &quot;   &quot; 100   &quot;</span></span><a href="#l67"></a>
<span id="l68"><span class="n">_DI4Y</span>   <span class="o">=</span> <span class="n">_days_before_year</span><span class="p">(</span><span class="mi">5</span><span class="p">)</span>      <span class="c">#    &quot;    &quot;   &quot;   &quot;   4   &quot;</span></span><a href="#l68"></a>
<span id="l69"></span><a href="#l69"></a>
<span id="l70"><span class="c"># A 4-year cycle has an extra leap day over what we&#39;d get from pasting</span></span><a href="#l70"></a>
<span id="l71"><span class="c"># together 4 single years.</span></span><a href="#l71"></a>
<span id="l72"><span class="k">assert</span> <span class="n">_DI4Y</span> <span class="o">==</span> <span class="mi">4</span> <span class="o">*</span> <span class="mi">365</span> <span class="o">+</span> <span class="mi">1</span></span><a href="#l72"></a>
<span id="l73"></span><a href="#l73"></a>
<span id="l74"><span class="c"># Similarly, a 400-year cycle has an extra leap day over what we&#39;d get from</span></span><a href="#l74"></a>
<span id="l75"><span class="c"># pasting together 4 100-year cycles.</span></span><a href="#l75"></a>
<span id="l76"><span class="k">assert</span> <span class="n">_DI400Y</span> <span class="o">==</span> <span class="mi">4</span> <span class="o">*</span> <span class="n">_DI100Y</span> <span class="o">+</span> <span class="mi">1</span></span><a href="#l76"></a>
<span id="l77"></span><a href="#l77"></a>
<span id="l78"><span class="c"># OTOH, a 100-year cycle has one fewer leap day than we&#39;d get from</span></span><a href="#l78"></a>
<span id="l79"><span class="c"># pasting together 25 4-year cycles.</span></span><a href="#l79"></a>
<span id="l80"><span class="k">assert</span> <span class="n">_DI100Y</span> <span class="o">==</span> <span class="mi">25</span> <span class="o">*</span> <span class="n">_DI4Y</span> <span class="o">-</span> <span class="mi">1</span></span><a href="#l80"></a>
<span id="l81"></span><a href="#l81"></a>
<span id="l82"><span class="k">def</span> <span class="nf">_ord2ymd</span><span class="p">(</span><span class="n">n</span><span class="p">):</span></span><a href="#l82"></a>
<span id="l83">    <span class="s">&quot;ordinal -&gt; (year, month, day), considering 01-Jan-0001 as day 1.&quot;</span></span><a href="#l83"></a>
<span id="l84"></span><a href="#l84"></a>
<span id="l85">    <span class="c"># n is a 1-based index, starting at 1-Jan-1.  The pattern of leap years</span></span><a href="#l85"></a>
<span id="l86">    <span class="c"># repeats exactly every 400 years.  The basic strategy is to find the</span></span><a href="#l86"></a>
<span id="l87">    <span class="c"># closest 400-year boundary at or before n, then work with the offset</span></span><a href="#l87"></a>
<span id="l88">    <span class="c"># from that boundary to n.  Life is much clearer if we subtract 1 from</span></span><a href="#l88"></a>
<span id="l89">    <span class="c"># n first -- then the values of n at 400-year boundaries are exactly</span></span><a href="#l89"></a>
<span id="l90">    <span class="c"># those divisible by _DI400Y:</span></span><a href="#l90"></a>
<span id="l91">    <span class="c">#</span></span><a href="#l91"></a>
<span id="l92">    <span class="c">#     D  M   Y            n              n-1</span></span><a href="#l92"></a>
<span id="l93">    <span class="c">#     -- --- ----        ----------     ----------------</span></span><a href="#l93"></a>
<span id="l94">    <span class="c">#     31 Dec -400        -_DI400Y       -_DI400Y -1</span></span><a href="#l94"></a>
<span id="l95">    <span class="c">#      1 Jan -399         -_DI400Y +1   -_DI400Y      400-year boundary</span></span><a href="#l95"></a>
<span id="l96">    <span class="c">#     ...</span></span><a href="#l96"></a>
<span id="l97">    <span class="c">#     30 Dec  000        -1             -2</span></span><a href="#l97"></a>
<span id="l98">    <span class="c">#     31 Dec  000         0             -1</span></span><a href="#l98"></a>
<span id="l99">    <span class="c">#      1 Jan  001         1              0            400-year boundary</span></span><a href="#l99"></a>
<span id="l100">    <span class="c">#      2 Jan  001         2              1</span></span><a href="#l100"></a>
<span id="l101">    <span class="c">#      3 Jan  001         3              2</span></span><a href="#l101"></a>
<span id="l102">    <span class="c">#     ...</span></span><a href="#l102"></a>
<span id="l103">    <span class="c">#     31 Dec  400         _DI400Y        _DI400Y -1</span></span><a href="#l103"></a>
<span id="l104">    <span class="c">#      1 Jan  401         _DI400Y +1     _DI400Y      400-year boundary</span></span><a href="#l104"></a>
<span id="l105">    <span class="n">n</span> <span class="o">-=</span> <span class="mi">1</span></span><a href="#l105"></a>
<span id="l106">    <span class="n">n400</span><span class="p">,</span> <span class="n">n</span> <span class="o">=</span> <span class="nb">divmod</span><span class="p">(</span><span class="n">n</span><span class="p">,</span> <span class="n">_DI400Y</span><span class="p">)</span></span><a href="#l106"></a>
<span id="l107">    <span class="n">year</span> <span class="o">=</span> <span class="n">n400</span> <span class="o">*</span> <span class="mi">400</span> <span class="o">+</span> <span class="mi">1</span>   <span class="c"># ..., -399, 1, 401, ...</span></span><a href="#l107"></a>
<span id="l108"></span><a href="#l108"></a>
<span id="l109">    <span class="c"># Now n is the (non-negative) offset, in days, from January 1 of year, to</span></span><a href="#l109"></a>
<span id="l110">    <span class="c"># the desired date.  Now compute how many 100-year cycles precede n.</span></span><a href="#l110"></a>
<span id="l111">    <span class="c"># Note that it&#39;s possible for n100 to equal 4!  In that case 4 full</span></span><a href="#l111"></a>
<span id="l112">    <span class="c"># 100-year cycles precede the desired day, which implies the desired</span></span><a href="#l112"></a>
<span id="l113">    <span class="c"># day is December 31 at the end of a 400-year cycle.</span></span><a href="#l113"></a>
<span id="l114">    <span class="n">n100</span><span class="p">,</span> <span class="n">n</span> <span class="o">=</span> <span class="nb">divmod</span><span class="p">(</span><span class="n">n</span><span class="p">,</span> <span class="n">_DI100Y</span><span class="p">)</span></span><a href="#l114"></a>
<span id="l115"></span><a href="#l115"></a>
<span id="l116">    <span class="c"># Now compute how many 4-year cycles precede it.</span></span><a href="#l116"></a>
<span id="l117">    <span class="n">n4</span><span class="p">,</span> <span class="n">n</span> <span class="o">=</span> <span class="nb">divmod</span><span class="p">(</span><span class="n">n</span><span class="p">,</span> <span class="n">_DI4Y</span><span class="p">)</span></span><a href="#l117"></a>
<span id="l118"></span><a href="#l118"></a>
<span id="l119">    <span class="c"># And now how many single years.  Again n1 can be 4, and again meaning</span></span><a href="#l119"></a>
<span id="l120">    <span class="c"># that the desired day is December 31 at the end of the 4-year cycle.</span></span><a href="#l120"></a>
<span id="l121">    <span class="n">n1</span><span class="p">,</span> <span class="n">n</span> <span class="o">=</span> <span class="nb">divmod</span><span class="p">(</span><span class="n">n</span><span class="p">,</span> <span class="mi">365</span><span class="p">)</span></span><a href="#l121"></a>
<span id="l122"></span><a href="#l122"></a>
<span id="l123">    <span class="n">year</span> <span class="o">+=</span> <span class="n">n100</span> <span class="o">*</span> <span class="mi">100</span> <span class="o">+</span> <span class="n">n4</span> <span class="o">*</span> <span class="mi">4</span> <span class="o">+</span> <span class="n">n1</span></span><a href="#l123"></a>
<span id="l124">    <span class="k">if</span> <span class="n">n1</span> <span class="o">==</span> <span class="mi">4</span> <span class="ow">or</span> <span class="n">n100</span> <span class="o">==</span> <span class="mi">4</span><span class="p">:</span></span><a href="#l124"></a>
<span id="l125">        <span class="k">assert</span> <span class="n">n</span> <span class="o">==</span> <span class="mi">0</span></span><a href="#l125"></a>
<span id="l126">        <span class="k">return</span> <span class="n">year</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="mi">12</span><span class="p">,</span> <span class="mi">31</span></span><a href="#l126"></a>
<span id="l127"></span><a href="#l127"></a>
<span id="l128">    <span class="c"># Now the year is correct, and n is the offset from January 1.  We find</span></span><a href="#l128"></a>
<span id="l129">    <span class="c"># the month via an estimate that&#39;s either exact or one too large.</span></span><a href="#l129"></a>
<span id="l130">    <span class="n">leapyear</span> <span class="o">=</span> <span class="n">n1</span> <span class="o">==</span> <span class="mi">3</span> <span class="ow">and</span> <span class="p">(</span><span class="n">n4</span> <span class="o">!=</span> <span class="mi">24</span> <span class="ow">or</span> <span class="n">n100</span> <span class="o">==</span> <span class="mi">3</span><span class="p">)</span></span><a href="#l130"></a>
<span id="l131">    <span class="k">assert</span> <span class="n">leapyear</span> <span class="o">==</span> <span class="n">_is_leap</span><span class="p">(</span><span class="n">year</span><span class="p">)</span></span><a href="#l131"></a>
<span id="l132">    <span class="n">month</span> <span class="o">=</span> <span class="p">(</span><span class="n">n</span> <span class="o">+</span> <span class="mi">50</span><span class="p">)</span> <span class="o">&gt;&gt;</span> <span class="mi">5</span></span><a href="#l132"></a>
<span id="l133">    <span class="n">preceding</span> <span class="o">=</span> <span class="n">_DAYS_BEFORE_MONTH</span><span class="p">[</span><span class="n">month</span><span class="p">]</span> <span class="o">+</span> <span class="p">(</span><span class="n">month</span> <span class="o">&gt;</span> <span class="mi">2</span> <span class="ow">and</span> <span class="n">leapyear</span><span class="p">)</span></span><a href="#l133"></a>
<span id="l134">    <span class="k">if</span> <span class="n">preceding</span> <span class="o">&gt;</span> <span class="n">n</span><span class="p">:</span>  <span class="c"># estimate is too large</span></span><a href="#l134"></a>
<span id="l135">        <span class="n">month</span> <span class="o">-=</span> <span class="mi">1</span></span><a href="#l135"></a>
<span id="l136">        <span class="n">preceding</span> <span class="o">-=</span> <span class="n">_DAYS_IN_MONTH</span><span class="p">[</span><span class="n">month</span><span class="p">]</span> <span class="o">+</span> <span class="p">(</span><span class="n">month</span> <span class="o">==</span> <span class="mi">2</span> <span class="ow">and</span> <span class="n">leapyear</span><span class="p">)</span></span><a href="#l136"></a>
<span id="l137">    <span class="n">n</span> <span class="o">-=</span> <span class="n">preceding</span></span><a href="#l137"></a>
<span id="l138">    <span class="k">assert</span> <span class="mi">0</span> <span class="o">&lt;=</span> <span class="n">n</span> <span class="o">&lt;</span> <span class="n">_days_in_month</span><span class="p">(</span><span class="n">year</span><span class="p">,</span> <span class="n">month</span><span class="p">)</span></span><a href="#l138"></a>
<span id="l139"></span><a href="#l139"></a>
<span id="l140">    <span class="c"># Now the year and month are correct, and n is the offset from the</span></span><a href="#l140"></a>
<span id="l141">    <span class="c"># start of that month:  we&#39;re done!</span></span><a href="#l141"></a>
<span id="l142">    <span class="k">return</span> <span class="n">year</span><span class="p">,</span> <span class="n">month</span><span class="p">,</span> <span class="n">n</span><span class="o">+</span><span class="mi">1</span></span><a href="#l142"></a>
<span id="l143"></span><a href="#l143"></a>
<span id="l144"><span class="c"># Month and day names.  For localized versions, see the calendar module.</span></span><a href="#l144"></a>
<span id="l145"><span class="n">_MONTHNAMES</span> <span class="o">=</span> <span class="p">[</span><span class="bp">None</span><span class="p">,</span> <span class="s">&quot;Jan&quot;</span><span class="p">,</span> <span class="s">&quot;Feb&quot;</span><span class="p">,</span> <span class="s">&quot;Mar&quot;</span><span class="p">,</span> <span class="s">&quot;Apr&quot;</span><span class="p">,</span> <span class="s">&quot;May&quot;</span><span class="p">,</span> <span class="s">&quot;Jun&quot;</span><span class="p">,</span></span><a href="#l145"></a>
<span id="l146">                     <span class="s">&quot;Jul&quot;</span><span class="p">,</span> <span class="s">&quot;Aug&quot;</span><span class="p">,</span> <span class="s">&quot;Sep&quot;</span><span class="p">,</span> <span class="s">&quot;Oct&quot;</span><span class="p">,</span> <span class="s">&quot;Nov&quot;</span><span class="p">,</span> <span class="s">&quot;Dec&quot;</span><span class="p">]</span></span><a href="#l146"></a>
<span id="l147"><span class="n">_DAYNAMES</span> <span class="o">=</span> <span class="p">[</span><span class="bp">None</span><span class="p">,</span> <span class="s">&quot;Mon&quot;</span><span class="p">,</span> <span class="s">&quot;Tue&quot;</span><span class="p">,</span> <span class="s">&quot;Wed&quot;</span><span class="p">,</span> <span class="s">&quot;Thu&quot;</span><span class="p">,</span> <span class="s">&quot;Fri&quot;</span><span class="p">,</span> <span class="s">&quot;Sat&quot;</span><span class="p">,</span> <span class="s">&quot;Sun&quot;</span><span class="p">]</span></span><a href="#l147"></a>
<span id="l148"></span><a href="#l148"></a>
<span id="l149"></span><a href="#l149"></a>
<span id="l150"><span class="k">def</span> <span class="nf">_build_struct_time</span><span class="p">(</span><span class="n">y</span><span class="p">,</span> <span class="n">m</span><span class="p">,</span> <span class="n">d</span><span class="p">,</span> <span class="n">hh</span><span class="p">,</span> <span class="n">mm</span><span class="p">,</span> <span class="n">ss</span><span class="p">,</span> <span class="n">dstflag</span><span class="p">):</span></span><a href="#l150"></a>
<span id="l151">    <span class="n">wday</span> <span class="o">=</span> <span class="p">(</span><span class="n">_ymd2ord</span><span class="p">(</span><span class="n">y</span><span class="p">,</span> <span class="n">m</span><span class="p">,</span> <span class="n">d</span><span class="p">)</span> <span class="o">+</span> <span class="mi">6</span><span class="p">)</span> <span class="o">%</span> <span class="mi">7</span></span><a href="#l151"></a>
<span id="l152">    <span class="n">dnum</span> <span class="o">=</span> <span class="n">_days_before_month</span><span class="p">(</span><span class="n">y</span><span class="p">,</span> <span class="n">m</span><span class="p">)</span> <span class="o">+</span> <span class="n">d</span></span><a href="#l152"></a>
<span id="l153">    <span class="k">return</span> <span class="n">_time</span><span class="o">.</span><span class="n">struct_time</span><span class="p">((</span><span class="n">y</span><span class="p">,</span> <span class="n">m</span><span class="p">,</span> <span class="n">d</span><span class="p">,</span> <span class="n">hh</span><span class="p">,</span> <span class="n">mm</span><span class="p">,</span> <span class="n">ss</span><span class="p">,</span> <span class="n">wday</span><span class="p">,</span> <span class="n">dnum</span><span class="p">,</span> <span class="n">dstflag</span><span class="p">))</span></span><a href="#l153"></a>
<span id="l154"></span><a href="#l154"></a>
<span id="l155"><span class="k">def</span> <span class="nf">_format_time</span><span class="p">(</span><span class="n">hh</span><span class="p">,</span> <span class="n">mm</span><span class="p">,</span> <span class="n">ss</span><span class="p">,</span> <span class="n">us</span><span class="p">):</span></span><a href="#l155"></a>
<span id="l156">    <span class="c"># Skip trailing microseconds when us==0.</span></span><a href="#l156"></a>
<span id="l157">    <span class="n">result</span> <span class="o">=</span> <span class="s">&quot;</span><span class="si">%02d</span><span class="s">:</span><span class="si">%02d</span><span class="s">:</span><span class="si">%02d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">hh</span><span class="p">,</span> <span class="n">mm</span><span class="p">,</span> <span class="n">ss</span><span class="p">)</span></span><a href="#l157"></a>
<span id="l158">    <span class="k">if</span> <span class="n">us</span><span class="p">:</span></span><a href="#l158"></a>
<span id="l159">        <span class="n">result</span> <span class="o">+=</span> <span class="s">&quot;.</span><span class="si">%06d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="n">us</span></span><a href="#l159"></a>
<span id="l160">    <span class="k">return</span> <span class="n">result</span></span><a href="#l160"></a>
<span id="l161"></span><a href="#l161"></a>
<span id="l162"><span class="c"># Correctly substitute for %z and %Z escapes in strftime formats.</span></span><a href="#l162"></a>
<span id="l163"><span class="k">def</span> <span class="nf">_wrap_strftime</span><span class="p">(</span><span class="nb">object</span><span class="p">,</span> <span class="n">format</span><span class="p">,</span> <span class="n">timetuple</span><span class="p">):</span></span><a href="#l163"></a>
<span id="l164">    <span class="c"># Don&#39;t call utcoffset() or tzname() unless actually needed.</span></span><a href="#l164"></a>
<span id="l165">    <span class="n">freplace</span> <span class="o">=</span> <span class="bp">None</span>  <span class="c"># the string to use for %f</span></span><a href="#l165"></a>
<span id="l166">    <span class="n">zreplace</span> <span class="o">=</span> <span class="bp">None</span>  <span class="c"># the string to use for %z</span></span><a href="#l166"></a>
<span id="l167">    <span class="n">Zreplace</span> <span class="o">=</span> <span class="bp">None</span>  <span class="c"># the string to use for %Z</span></span><a href="#l167"></a>
<span id="l168"></span><a href="#l168"></a>
<span id="l169">    <span class="c"># Scan format for %z and %Z escapes, replacing as needed.</span></span><a href="#l169"></a>
<span id="l170">    <span class="n">newformat</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l170"></a>
<span id="l171">    <span class="n">push</span> <span class="o">=</span> <span class="n">newformat</span><span class="o">.</span><span class="n">append</span></span><a href="#l171"></a>
<span id="l172">    <span class="n">i</span><span class="p">,</span> <span class="n">n</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">format</span><span class="p">)</span></span><a href="#l172"></a>
<span id="l173">    <span class="k">while</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">n</span><span class="p">:</span></span><a href="#l173"></a>
<span id="l174">        <span class="n">ch</span> <span class="o">=</span> <span class="n">format</span><span class="p">[</span><span class="n">i</span><span class="p">]</span></span><a href="#l174"></a>
<span id="l175">        <span class="n">i</span> <span class="o">+=</span> <span class="mi">1</span></span><a href="#l175"></a>
<span id="l176">        <span class="k">if</span> <span class="n">ch</span> <span class="o">==</span> <span class="s">&#39;%&#39;</span><span class="p">:</span></span><a href="#l176"></a>
<span id="l177">            <span class="k">if</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">n</span><span class="p">:</span></span><a href="#l177"></a>
<span id="l178">                <span class="n">ch</span> <span class="o">=</span> <span class="n">format</span><span class="p">[</span><span class="n">i</span><span class="p">]</span></span><a href="#l178"></a>
<span id="l179">                <span class="n">i</span> <span class="o">+=</span> <span class="mi">1</span></span><a href="#l179"></a>
<span id="l180">                <span class="k">if</span> <span class="n">ch</span> <span class="o">==</span> <span class="s">&#39;f&#39;</span><span class="p">:</span></span><a href="#l180"></a>
<span id="l181">                    <span class="k">if</span> <span class="n">freplace</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l181"></a>
<span id="l182">                        <span class="n">freplace</span> <span class="o">=</span> <span class="s">&#39;</span><span class="si">%06d</span><span class="s">&#39;</span> <span class="o">%</span> <span class="nb">getattr</span><span class="p">(</span><span class="nb">object</span><span class="p">,</span></span><a href="#l182"></a>
<span id="l183">                                                    <span class="s">&#39;microsecond&#39;</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span></span><a href="#l183"></a>
<span id="l184">                    <span class="n">newformat</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">freplace</span><span class="p">)</span></span><a href="#l184"></a>
<span id="l185">                <span class="k">elif</span> <span class="n">ch</span> <span class="o">==</span> <span class="s">&#39;z&#39;</span><span class="p">:</span></span><a href="#l185"></a>
<span id="l186">                    <span class="k">if</span> <span class="n">zreplace</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l186"></a>
<span id="l187">                        <span class="n">zreplace</span> <span class="o">=</span> <span class="s">&quot;&quot;</span></span><a href="#l187"></a>
<span id="l188">                        <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="nb">object</span><span class="p">,</span> <span class="s">&quot;utcoffset&quot;</span><span class="p">):</span></span><a href="#l188"></a>
<span id="l189">                            <span class="n">offset</span> <span class="o">=</span> <span class="nb">object</span><span class="o">.</span><span class="n">utcoffset</span><span class="p">()</span></span><a href="#l189"></a>
<span id="l190">                            <span class="k">if</span> <span class="n">offset</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l190"></a>
<span id="l191">                                <span class="n">sign</span> <span class="o">=</span> <span class="s">&#39;+&#39;</span></span><a href="#l191"></a>
<span id="l192">                                <span class="k">if</span> <span class="n">offset</span><span class="o">.</span><span class="n">days</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span></span><a href="#l192"></a>
<span id="l193">                                    <span class="n">offset</span> <span class="o">=</span> <span class="o">-</span><span class="n">offset</span></span><a href="#l193"></a>
<span id="l194">                                    <span class="n">sign</span> <span class="o">=</span> <span class="s">&#39;-&#39;</span></span><a href="#l194"></a>
<span id="l195">                                <span class="n">h</span><span class="p">,</span> <span class="n">m</span> <span class="o">=</span> <span class="nb">divmod</span><span class="p">(</span><span class="n">offset</span><span class="p">,</span> <span class="n">timedelta</span><span class="p">(</span><span class="n">hours</span><span class="o">=</span><span class="mi">1</span><span class="p">))</span></span><a href="#l195"></a>
<span id="l196">                                <span class="k">assert</span> <span class="ow">not</span> <span class="n">m</span> <span class="o">%</span> <span class="n">timedelta</span><span class="p">(</span><span class="n">minutes</span><span class="o">=</span><span class="mi">1</span><span class="p">),</span> <span class="s">&quot;whole minute&quot;</span></span><a href="#l196"></a>
<span id="l197">                                <span class="n">m</span> <span class="o">//=</span> <span class="n">timedelta</span><span class="p">(</span><span class="n">minutes</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span></span><a href="#l197"></a>
<span id="l198">                                <span class="n">zreplace</span> <span class="o">=</span> <span class="s">&#39;</span><span class="si">%c%02d%02d</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">sign</span><span class="p">,</span> <span class="n">h</span><span class="p">,</span> <span class="n">m</span><span class="p">)</span></span><a href="#l198"></a>
<span id="l199">                    <span class="k">assert</span> <span class="s">&#39;%&#39;</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">zreplace</span></span><a href="#l199"></a>
<span id="l200">                    <span class="n">newformat</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">zreplace</span><span class="p">)</span></span><a href="#l200"></a>
<span id="l201">                <span class="k">elif</span> <span class="n">ch</span> <span class="o">==</span> <span class="s">&#39;Z&#39;</span><span class="p">:</span></span><a href="#l201"></a>
<span id="l202">                    <span class="k">if</span> <span class="n">Zreplace</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l202"></a>
<span id="l203">                        <span class="n">Zreplace</span> <span class="o">=</span> <span class="s">&quot;&quot;</span></span><a href="#l203"></a>
<span id="l204">                        <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="nb">object</span><span class="p">,</span> <span class="s">&quot;tzname&quot;</span><span class="p">):</span></span><a href="#l204"></a>
<span id="l205">                            <span class="n">s</span> <span class="o">=</span> <span class="nb">object</span><span class="o">.</span><span class="n">tzname</span><span class="p">()</span></span><a href="#l205"></a>
<span id="l206">                            <span class="k">if</span> <span class="n">s</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l206"></a>
<span id="l207">                                <span class="c"># strftime is going to have at this: escape %</span></span><a href="#l207"></a>
<span id="l208">                                <span class="n">Zreplace</span> <span class="o">=</span> <span class="n">s</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&#39;%&#39;</span><span class="p">,</span> <span class="s">&#39;</span><span class="si">%%</span><span class="s">&#39;</span><span class="p">)</span></span><a href="#l208"></a>
<span id="l209">                    <span class="n">newformat</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">Zreplace</span><span class="p">)</span></span><a href="#l209"></a>
<span id="l210">                <span class="k">else</span><span class="p">:</span></span><a href="#l210"></a>
<span id="l211">                    <span class="n">push</span><span class="p">(</span><span class="s">&#39;%&#39;</span><span class="p">)</span></span><a href="#l211"></a>
<span id="l212">                    <span class="n">push</span><span class="p">(</span><span class="n">ch</span><span class="p">)</span></span><a href="#l212"></a>
<span id="l213">            <span class="k">else</span><span class="p">:</span></span><a href="#l213"></a>
<span id="l214">                <span class="n">push</span><span class="p">(</span><span class="s">&#39;%&#39;</span><span class="p">)</span></span><a href="#l214"></a>
<span id="l215">        <span class="k">else</span><span class="p">:</span></span><a href="#l215"></a>
<span id="l216">            <span class="n">push</span><span class="p">(</span><span class="n">ch</span><span class="p">)</span></span><a href="#l216"></a>
<span id="l217">    <span class="n">newformat</span> <span class="o">=</span> <span class="s">&quot;&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">newformat</span><span class="p">)</span></span><a href="#l217"></a>
<span id="l218">    <span class="k">return</span> <span class="n">_time</span><span class="o">.</span><span class="n">strftime</span><span class="p">(</span><span class="n">newformat</span><span class="p">,</span> <span class="n">timetuple</span><span class="p">)</span></span><a href="#l218"></a>
<span id="l219"></span><a href="#l219"></a>
<span id="l220"><span class="c"># Just raise TypeError if the arg isn&#39;t None or a string.</span></span><a href="#l220"></a>
<span id="l221"><span class="k">def</span> <span class="nf">_check_tzname</span><span class="p">(</span><span class="n">name</span><span class="p">):</span></span><a href="#l221"></a>
<span id="l222">    <span class="k">if</span> <span class="n">name</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span> <span class="ow">and</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span></span><a href="#l222"></a>
<span id="l223">        <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="s">&quot;tzinfo.tzname() must return None or string, &quot;</span></span><a href="#l223"></a>
<span id="l224">                        <span class="s">&quot;not &#39;</span><span class="si">%s</span><span class="s">&#39;&quot;</span> <span class="o">%</span> <span class="nb">type</span><span class="p">(</span><span class="n">name</span><span class="p">))</span></span><a href="#l224"></a>
<span id="l225"></span><a href="#l225"></a>
<span id="l226"><span class="c"># name is the offset-producing method, &quot;utcoffset&quot; or &quot;dst&quot;.</span></span><a href="#l226"></a>
<span id="l227"><span class="c"># offset is what it returned.</span></span><a href="#l227"></a>
<span id="l228"><span class="c"># If offset isn&#39;t None or timedelta, raises TypeError.</span></span><a href="#l228"></a>
<span id="l229"><span class="c"># If offset is None, returns None.</span></span><a href="#l229"></a>
<span id="l230"><span class="c"># Else offset is checked for being in range, and a whole # of minutes.</span></span><a href="#l230"></a>
<span id="l231"><span class="c"># If it is, its integer value is returned.  Else ValueError is raised.</span></span><a href="#l231"></a>
<span id="l232"><span class="k">def</span> <span class="nf">_check_utc_offset</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">offset</span><span class="p">):</span></span><a href="#l232"></a>
<span id="l233">    <span class="k">assert</span> <span class="n">name</span> <span class="ow">in</span> <span class="p">(</span><span class="s">&quot;utcoffset&quot;</span><span class="p">,</span> <span class="s">&quot;dst&quot;</span><span class="p">)</span></span><a href="#l233"></a>
<span id="l234">    <span class="k">if</span> <span class="n">offset</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l234"></a>
<span id="l235">        <span class="k">return</span></span><a href="#l235"></a>
<span id="l236">    <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">offset</span><span class="p">,</span> <span class="n">timedelta</span><span class="p">):</span></span><a href="#l236"></a>
<span id="l237">        <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="s">&quot;tzinfo.</span><span class="si">%s</span><span class="s">() must return None &quot;</span></span><a href="#l237"></a>
<span id="l238">                        <span class="s">&quot;or timedelta, not &#39;</span><span class="si">%s</span><span class="s">&#39;&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="nb">type</span><span class="p">(</span><span class="n">offset</span><span class="p">)))</span></span><a href="#l238"></a>
<span id="l239">    <span class="k">if</span> <span class="n">offset</span> <span class="o">%</span> <span class="n">timedelta</span><span class="p">(</span><span class="n">minutes</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span> <span class="ow">or</span> <span class="n">offset</span><span class="o">.</span><span class="n">microseconds</span><span class="p">:</span></span><a href="#l239"></a>
<span id="l240">        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&quot;tzinfo.</span><span class="si">%s</span><span class="s">() must return a whole number &quot;</span></span><a href="#l240"></a>
<span id="l241">                         <span class="s">&quot;of minutes, got </span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">offset</span><span class="p">))</span></span><a href="#l241"></a>
<span id="l242">    <span class="k">if</span> <span class="ow">not</span> <span class="o">-</span><span class="n">timedelta</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span> <span class="o">&lt;</span> <span class="n">offset</span> <span class="o">&lt;</span> <span class="n">timedelta</span><span class="p">(</span><span class="mi">1</span><span class="p">):</span></span><a href="#l242"></a>
<span id="l243">        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&quot;</span><span class="si">%s</span><span class="s">()=</span><span class="si">%s</span><span class="s">, must be must be strictly between &quot;</span></span><a href="#l243"></a>
<span id="l244">                         <span class="s">&quot;-timedelta(hours=24) and timedelta(hours=24)&quot;</span> <span class="o">%</span></span><a href="#l244"></a>
<span id="l245">                         <span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">offset</span><span class="p">))</span></span><a href="#l245"></a>
<span id="l246"></span><a href="#l246"></a>
<span id="l247"><span class="k">def</span> <span class="nf">_check_int_field</span><span class="p">(</span><span class="n">value</span><span class="p">):</span></span><a href="#l247"></a>
<span id="l248">    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="nb">int</span><span class="p">):</span></span><a href="#l248"></a>
<span id="l249">        <span class="k">return</span> <span class="n">value</span></span><a href="#l249"></a>
<span id="l250">    <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="nb">float</span><span class="p">):</span></span><a href="#l250"></a>
<span id="l251">        <span class="k">try</span><span class="p">:</span></span><a href="#l251"></a>
<span id="l252">            <span class="n">value</span> <span class="o">=</span> <span class="n">value</span><span class="o">.</span><span class="n">__int__</span><span class="p">()</span></span><a href="#l252"></a>
<span id="l253">        <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span></span><a href="#l253"></a>
<span id="l254">            <span class="k">pass</span></span><a href="#l254"></a>
<span id="l255">        <span class="k">else</span><span class="p">:</span></span><a href="#l255"></a>
<span id="l256">            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="nb">int</span><span class="p">):</span></span><a href="#l256"></a>
<span id="l257">                <span class="k">return</span> <span class="n">value</span></span><a href="#l257"></a>
<span id="l258">            <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="s">&#39;__int__ returned non-int (type </span><span class="si">%s</span><span class="s">)&#39;</span> <span class="o">%</span></span><a href="#l258"></a>
<span id="l259">                            <span class="nb">type</span><span class="p">(</span><span class="n">value</span><span class="p">)</span><span class="o">.</span><span class="n">__name__</span><span class="p">)</span></span><a href="#l259"></a>
<span id="l260">        <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="s">&#39;an integer is required (got type </span><span class="si">%s</span><span class="s">)&#39;</span> <span class="o">%</span></span><a href="#l260"></a>
<span id="l261">                        <span class="nb">type</span><span class="p">(</span><span class="n">value</span><span class="p">)</span><span class="o">.</span><span class="n">__name__</span><span class="p">)</span></span><a href="#l261"></a>
<span id="l262">    <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="s">&#39;integer argument expected, got float&#39;</span><span class="p">)</span></span><a href="#l262"></a>
<span id="l263"></span><a href="#l263"></a>
<span id="l264"><span class="k">def</span> <span class="nf">_check_date_fields</span><span class="p">(</span><span class="n">year</span><span class="p">,</span> <span class="n">month</span><span class="p">,</span> <span class="n">day</span><span class="p">):</span></span><a href="#l264"></a>
<span id="l265">    <span class="n">year</span> <span class="o">=</span> <span class="n">_check_int_field</span><span class="p">(</span><span class="n">year</span><span class="p">)</span></span><a href="#l265"></a>
<span id="l266">    <span class="n">month</span> <span class="o">=</span> <span class="n">_check_int_field</span><span class="p">(</span><span class="n">month</span><span class="p">)</span></span><a href="#l266"></a>
<span id="l267">    <span class="n">day</span> <span class="o">=</span> <span class="n">_check_int_field</span><span class="p">(</span><span class="n">day</span><span class="p">)</span></span><a href="#l267"></a>
<span id="l268">    <span class="k">if</span> <span class="ow">not</span> <span class="n">MINYEAR</span> <span class="o">&lt;=</span> <span class="n">year</span> <span class="o">&lt;=</span> <span class="n">MAXYEAR</span><span class="p">:</span></span><a href="#l268"></a>
<span id="l269">        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&#39;year must be in </span><span class="si">%d</span><span class="s">..</span><span class="si">%d</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">MINYEAR</span><span class="p">,</span> <span class="n">MAXYEAR</span><span class="p">),</span> <span class="n">year</span><span class="p">)</span></span><a href="#l269"></a>
<span id="l270">    <span class="k">if</span> <span class="ow">not</span> <span class="mi">1</span> <span class="o">&lt;=</span> <span class="n">month</span> <span class="o">&lt;=</span> <span class="mi">12</span><span class="p">:</span></span><a href="#l270"></a>
<span id="l271">        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&#39;month must be in 1..12&#39;</span><span class="p">,</span> <span class="n">month</span><span class="p">)</span></span><a href="#l271"></a>
<span id="l272">    <span class="n">dim</span> <span class="o">=</span> <span class="n">_days_in_month</span><span class="p">(</span><span class="n">year</span><span class="p">,</span> <span class="n">month</span><span class="p">)</span></span><a href="#l272"></a>
<span id="l273">    <span class="k">if</span> <span class="ow">not</span> <span class="mi">1</span> <span class="o">&lt;=</span> <span class="n">day</span> <span class="o">&lt;=</span> <span class="n">dim</span><span class="p">:</span></span><a href="#l273"></a>
<span id="l274">        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&#39;day must be in 1..</span><span class="si">%d</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">dim</span><span class="p">,</span> <span class="n">day</span><span class="p">)</span></span><a href="#l274"></a>
<span id="l275">    <span class="k">return</span> <span class="n">year</span><span class="p">,</span> <span class="n">month</span><span class="p">,</span> <span class="n">day</span></span><a href="#l275"></a>
<span id="l276"></span><a href="#l276"></a>
<span id="l277"><span class="k">def</span> <span class="nf">_check_time_fields</span><span class="p">(</span><span class="n">hour</span><span class="p">,</span> <span class="n">minute</span><span class="p">,</span> <span class="n">second</span><span class="p">,</span> <span class="n">microsecond</span><span class="p">):</span></span><a href="#l277"></a>
<span id="l278">    <span class="n">hour</span> <span class="o">=</span> <span class="n">_check_int_field</span><span class="p">(</span><span class="n">hour</span><span class="p">)</span></span><a href="#l278"></a>
<span id="l279">    <span class="n">minute</span> <span class="o">=</span> <span class="n">_check_int_field</span><span class="p">(</span><span class="n">minute</span><span class="p">)</span></span><a href="#l279"></a>
<span id="l280">    <span class="n">second</span> <span class="o">=</span> <span class="n">_check_int_field</span><span class="p">(</span><span class="n">second</span><span class="p">)</span></span><a href="#l280"></a>
<span id="l281">    <span class="n">microsecond</span> <span class="o">=</span> <span class="n">_check_int_field</span><span class="p">(</span><span class="n">microsecond</span><span class="p">)</span></span><a href="#l281"></a>
<span id="l282">    <span class="k">if</span> <span class="ow">not</span> <span class="mi">0</span> <span class="o">&lt;=</span> <span class="n">hour</span> <span class="o">&lt;=</span> <span class="mi">23</span><span class="p">:</span></span><a href="#l282"></a>
<span id="l283">        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&#39;hour must be in 0..23&#39;</span><span class="p">,</span> <span class="n">hour</span><span class="p">)</span></span><a href="#l283"></a>
<span id="l284">    <span class="k">if</span> <span class="ow">not</span> <span class="mi">0</span> <span class="o">&lt;=</span> <span class="n">minute</span> <span class="o">&lt;=</span> <span class="mi">59</span><span class="p">:</span></span><a href="#l284"></a>
<span id="l285">        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&#39;minute must be in 0..59&#39;</span><span class="p">,</span> <span class="n">minute</span><span class="p">)</span></span><a href="#l285"></a>
<span id="l286">    <span class="k">if</span> <span class="ow">not</span> <span class="mi">0</span> <span class="o">&lt;=</span> <span class="n">second</span> <span class="o">&lt;=</span> <span class="mi">59</span><span class="p">:</span></span><a href="#l286"></a>
<span id="l287">        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&#39;second must be in 0..59&#39;</span><span class="p">,</span> <span class="n">second</span><span class="p">)</span></span><a href="#l287"></a>
<span id="l288">    <span class="k">if</span> <span class="ow">not</span> <span class="mi">0</span> <span class="o">&lt;=</span> <span class="n">microsecond</span> <span class="o">&lt;=</span> <span class="mi">999999</span><span class="p">:</span></span><a href="#l288"></a>
<span id="l289">        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&#39;microsecond must be in 0..999999&#39;</span><span class="p">,</span> <span class="n">microsecond</span><span class="p">)</span></span><a href="#l289"></a>
<span id="l290">    <span class="k">return</span> <span class="n">hour</span><span class="p">,</span> <span class="n">minute</span><span class="p">,</span> <span class="n">second</span><span class="p">,</span> <span class="n">microsecond</span></span><a href="#l290"></a>
<span id="l291"></span><a href="#l291"></a>
<span id="l292"><span class="k">def</span> <span class="nf">_check_tzinfo_arg</span><span class="p">(</span><span class="n">tz</span><span class="p">):</span></span><a href="#l292"></a>
<span id="l293">    <span class="k">if</span> <span class="n">tz</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span> <span class="ow">and</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">tz</span><span class="p">,</span> <span class="n">tzinfo</span><span class="p">):</span></span><a href="#l293"></a>
<span id="l294">        <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="s">&quot;tzinfo argument must be None or of a tzinfo subclass&quot;</span><span class="p">)</span></span><a href="#l294"></a>
<span id="l295"></span><a href="#l295"></a>
<span id="l296"><span class="k">def</span> <span class="nf">_cmperror</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">):</span></span><a href="#l296"></a>
<span id="l297">    <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="s">&quot;can&#39;t compare &#39;</span><span class="si">%s</span><span class="s">&#39; to &#39;</span><span class="si">%s</span><span class="s">&#39;&quot;</span> <span class="o">%</span> <span class="p">(</span></span><a href="#l297"></a>
<span id="l298">                    <span class="nb">type</span><span class="p">(</span><span class="n">x</span><span class="p">)</span><span class="o">.</span><span class="n">__name__</span><span class="p">,</span> <span class="nb">type</span><span class="p">(</span><span class="n">y</span><span class="p">)</span><span class="o">.</span><span class="n">__name__</span><span class="p">))</span></span><a href="#l298"></a>
<span id="l299"></span><a href="#l299"></a>
<span id="l300"><span class="k">def</span> <span class="nf">_divide_and_round</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">):</span></span><a href="#l300"></a>
<span id="l301">    <span class="sd">&quot;&quot;&quot;divide a by b and round result to the nearest integer</span></span><a href="#l301"></a>
<span id="l302"></span><a href="#l302"></a>
<span id="l303"><span class="sd">    When the ratio is exactly half-way between two integers,</span></span><a href="#l303"></a>
<span id="l304"><span class="sd">    the even integer is returned.</span></span><a href="#l304"></a>
<span id="l305"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l305"></a>
<span id="l306">    <span class="c"># Based on the reference implementation for divmod_near</span></span><a href="#l306"></a>
<span id="l307">    <span class="c"># in Objects/longobject.c.</span></span><a href="#l307"></a>
<span id="l308">    <span class="n">q</span><span class="p">,</span> <span class="n">r</span> <span class="o">=</span> <span class="nb">divmod</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">)</span></span><a href="#l308"></a>
<span id="l309">    <span class="c"># round up if either r / b &gt; 0.5, or r / b == 0.5 and q is odd.</span></span><a href="#l309"></a>
<span id="l310">    <span class="c"># The expression r / b &gt; 0.5 is equivalent to 2 * r &gt; b if b is</span></span><a href="#l310"></a>
<span id="l311">    <span class="c"># positive, 2 * r &lt; b if b negative.</span></span><a href="#l311"></a>
<span id="l312">    <span class="n">r</span> <span class="o">*=</span> <span class="mi">2</span></span><a href="#l312"></a>
<span id="l313">    <span class="n">greater_than_half</span> <span class="o">=</span> <span class="n">r</span> <span class="o">&gt;</span> <span class="n">b</span> <span class="k">if</span> <span class="n">b</span> <span class="o">&gt;</span> <span class="mi">0</span> <span class="k">else</span> <span class="n">r</span> <span class="o">&lt;</span> <span class="n">b</span></span><a href="#l313"></a>
<span id="l314">    <span class="k">if</span> <span class="n">greater_than_half</span> <span class="ow">or</span> <span class="n">r</span> <span class="o">==</span> <span class="n">b</span> <span class="ow">and</span> <span class="n">q</span> <span class="o">%</span> <span class="mi">2</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span></span><a href="#l314"></a>
<span id="l315">        <span class="n">q</span> <span class="o">+=</span> <span class="mi">1</span></span><a href="#l315"></a>
<span id="l316"></span><a href="#l316"></a>
<span id="l317">    <span class="k">return</span> <span class="n">q</span></span><a href="#l317"></a>
<span id="l318"></span><a href="#l318"></a>
<span id="l319"><span class="k">class</span> <span class="nc">timedelta</span><span class="p">:</span></span><a href="#l319"></a>
<span id="l320">    <span class="sd">&quot;&quot;&quot;Represent the difference between two datetime objects.</span></span><a href="#l320"></a>
<span id="l321"></span><a href="#l321"></a>
<span id="l322"><span class="sd">    Supported operators:</span></span><a href="#l322"></a>
<span id="l323"></span><a href="#l323"></a>
<span id="l324"><span class="sd">    - add, subtract timedelta</span></span><a href="#l324"></a>
<span id="l325"><span class="sd">    - unary plus, minus, abs</span></span><a href="#l325"></a>
<span id="l326"><span class="sd">    - compare to timedelta</span></span><a href="#l326"></a>
<span id="l327"><span class="sd">    - multiply, divide by int</span></span><a href="#l327"></a>
<span id="l328"></span><a href="#l328"></a>
<span id="l329"><span class="sd">    In addition, datetime supports subtraction of two datetime objects</span></span><a href="#l329"></a>
<span id="l330"><span class="sd">    returning a timedelta, and addition or subtraction of a datetime</span></span><a href="#l330"></a>
<span id="l331"><span class="sd">    and a timedelta giving a datetime.</span></span><a href="#l331"></a>
<span id="l332"></span><a href="#l332"></a>
<span id="l333"><span class="sd">    Representation: (days, seconds, microseconds).  Why?  Because I</span></span><a href="#l333"></a>
<span id="l334"><span class="sd">    felt like it.</span></span><a href="#l334"></a>
<span id="l335"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l335"></a>
<span id="l336">    <span class="n">__slots__</span> <span class="o">=</span> <span class="s">&#39;_days&#39;</span><span class="p">,</span> <span class="s">&#39;_seconds&#39;</span><span class="p">,</span> <span class="s">&#39;_microseconds&#39;</span><span class="p">,</span> <span class="s">&#39;_hashcode&#39;</span></span><a href="#l336"></a>
<span id="l337"></span><a href="#l337"></a>
<span id="l338">    <span class="k">def</span> <span class="nf">__new__</span><span class="p">(</span><span class="n">cls</span><span class="p">,</span> <span class="n">days</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">seconds</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">microseconds</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span></span><a href="#l338"></a>
<span id="l339">                <span class="n">milliseconds</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">minutes</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">hours</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">weeks</span><span class="o">=</span><span class="mi">0</span><span class="p">):</span></span><a href="#l339"></a>
<span id="l340">        <span class="c"># Doing this efficiently and accurately in C is going to be difficult</span></span><a href="#l340"></a>
<span id="l341">        <span class="c"># and error-prone, due to ubiquitous overflow possibilities, and that</span></span><a href="#l341"></a>
<span id="l342">        <span class="c"># C double doesn&#39;t have enough bits of precision to represent</span></span><a href="#l342"></a>
<span id="l343">        <span class="c"># microseconds over 10K years faithfully.  The code here tries to make</span></span><a href="#l343"></a>
<span id="l344">        <span class="c"># explicit where go-fast assumptions can be relied on, in order to</span></span><a href="#l344"></a>
<span id="l345">        <span class="c"># guide the C implementation; it&#39;s way more convoluted than speed-</span></span><a href="#l345"></a>
<span id="l346">        <span class="c"># ignoring auto-overflow-to-long idiomatic Python could be.</span></span><a href="#l346"></a>
<span id="l347"></span><a href="#l347"></a>
<span id="l348">        <span class="c"># XXX Check that all inputs are ints or floats.</span></span><a href="#l348"></a>
<span id="l349"></span><a href="#l349"></a>
<span id="l350">        <span class="c"># Final values, all integer.</span></span><a href="#l350"></a>
<span id="l351">        <span class="c"># s and us fit in 32-bit signed ints; d isn&#39;t bounded.</span></span><a href="#l351"></a>
<span id="l352">        <span class="n">d</span> <span class="o">=</span> <span class="n">s</span> <span class="o">=</span> <span class="n">us</span> <span class="o">=</span> <span class="mi">0</span></span><a href="#l352"></a>
<span id="l353"></span><a href="#l353"></a>
<span id="l354">        <span class="c"># Normalize everything to days, seconds, microseconds.</span></span><a href="#l354"></a>
<span id="l355">        <span class="n">days</span> <span class="o">+=</span> <span class="n">weeks</span><span class="o">*</span><span class="mi">7</span></span><a href="#l355"></a>
<span id="l356">        <span class="n">seconds</span> <span class="o">+=</span> <span class="n">minutes</span><span class="o">*</span><span class="mi">60</span> <span class="o">+</span> <span class="n">hours</span><span class="o">*</span><span class="mi">3600</span></span><a href="#l356"></a>
<span id="l357">        <span class="n">microseconds</span> <span class="o">+=</span> <span class="n">milliseconds</span><span class="o">*</span><span class="mi">1000</span></span><a href="#l357"></a>
<span id="l358"></span><a href="#l358"></a>
<span id="l359">        <span class="c"># Get rid of all fractions, and normalize s and us.</span></span><a href="#l359"></a>
<span id="l360">        <span class="c"># Take a deep breath &lt;wink&gt;.</span></span><a href="#l360"></a>
<span id="l361">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">days</span><span class="p">,</span> <span class="nb">float</span><span class="p">):</span></span><a href="#l361"></a>
<span id="l362">            <span class="n">dayfrac</span><span class="p">,</span> <span class="n">days</span> <span class="o">=</span> <span class="n">_math</span><span class="o">.</span><span class="n">modf</span><span class="p">(</span><span class="n">days</span><span class="p">)</span></span><a href="#l362"></a>
<span id="l363">            <span class="n">daysecondsfrac</span><span class="p">,</span> <span class="n">daysecondswhole</span> <span class="o">=</span> <span class="n">_math</span><span class="o">.</span><span class="n">modf</span><span class="p">(</span><span class="n">dayfrac</span> <span class="o">*</span> <span class="p">(</span><span class="mf">24.</span><span class="o">*</span><span class="mf">3600.</span><span class="p">))</span></span><a href="#l363"></a>
<span id="l364">            <span class="k">assert</span> <span class="n">daysecondswhole</span> <span class="o">==</span> <span class="nb">int</span><span class="p">(</span><span class="n">daysecondswhole</span><span class="p">)</span>  <span class="c"># can&#39;t overflow</span></span><a href="#l364"></a>
<span id="l365">            <span class="n">s</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">daysecondswhole</span><span class="p">)</span></span><a href="#l365"></a>
<span id="l366">            <span class="k">assert</span> <span class="n">days</span> <span class="o">==</span> <span class="nb">int</span><span class="p">(</span><span class="n">days</span><span class="p">)</span></span><a href="#l366"></a>
<span id="l367">            <span class="n">d</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">days</span><span class="p">)</span></span><a href="#l367"></a>
<span id="l368">        <span class="k">else</span><span class="p">:</span></span><a href="#l368"></a>
<span id="l369">            <span class="n">daysecondsfrac</span> <span class="o">=</span> <span class="mf">0.0</span></span><a href="#l369"></a>
<span id="l370">            <span class="n">d</span> <span class="o">=</span> <span class="n">days</span></span><a href="#l370"></a>
<span id="l371">        <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">daysecondsfrac</span><span class="p">,</span> <span class="nb">float</span><span class="p">)</span></span><a href="#l371"></a>
<span id="l372">        <span class="k">assert</span> <span class="nb">abs</span><span class="p">(</span><span class="n">daysecondsfrac</span><span class="p">)</span> <span class="o">&lt;=</span> <span class="mf">1.0</span></span><a href="#l372"></a>
<span id="l373">        <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">d</span><span class="p">,</span> <span class="nb">int</span><span class="p">)</span></span><a href="#l373"></a>
<span id="l374">        <span class="k">assert</span> <span class="nb">abs</span><span class="p">(</span><span class="n">s</span><span class="p">)</span> <span class="o">&lt;=</span> <span class="mi">24</span> <span class="o">*</span> <span class="mi">3600</span></span><a href="#l374"></a>
<span id="l375">        <span class="c"># days isn&#39;t referenced again before redefinition</span></span><a href="#l375"></a>
<span id="l376"></span><a href="#l376"></a>
<span id="l377">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">seconds</span><span class="p">,</span> <span class="nb">float</span><span class="p">):</span></span><a href="#l377"></a>
<span id="l378">            <span class="n">secondsfrac</span><span class="p">,</span> <span class="n">seconds</span> <span class="o">=</span> <span class="n">_math</span><span class="o">.</span><span class="n">modf</span><span class="p">(</span><span class="n">seconds</span><span class="p">)</span></span><a href="#l378"></a>
<span id="l379">            <span class="k">assert</span> <span class="n">seconds</span> <span class="o">==</span> <span class="nb">int</span><span class="p">(</span><span class="n">seconds</span><span class="p">)</span></span><a href="#l379"></a>
<span id="l380">            <span class="n">seconds</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">seconds</span><span class="p">)</span></span><a href="#l380"></a>
<span id="l381">            <span class="n">secondsfrac</span> <span class="o">+=</span> <span class="n">daysecondsfrac</span></span><a href="#l381"></a>
<span id="l382">            <span class="k">assert</span> <span class="nb">abs</span><span class="p">(</span><span class="n">secondsfrac</span><span class="p">)</span> <span class="o">&lt;=</span> <span class="mf">2.0</span></span><a href="#l382"></a>
<span id="l383">        <span class="k">else</span><span class="p">:</span></span><a href="#l383"></a>
<span id="l384">            <span class="n">secondsfrac</span> <span class="o">=</span> <span class="n">daysecondsfrac</span></span><a href="#l384"></a>
<span id="l385">        <span class="c"># daysecondsfrac isn&#39;t referenced again</span></span><a href="#l385"></a>
<span id="l386">        <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">secondsfrac</span><span class="p">,</span> <span class="nb">float</span><span class="p">)</span></span><a href="#l386"></a>
<span id="l387">        <span class="k">assert</span> <span class="nb">abs</span><span class="p">(</span><span class="n">secondsfrac</span><span class="p">)</span> <span class="o">&lt;=</span> <span class="mf">2.0</span></span><a href="#l387"></a>
<span id="l388"></span><a href="#l388"></a>
<span id="l389">        <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">seconds</span><span class="p">,</span> <span class="nb">int</span><span class="p">)</span></span><a href="#l389"></a>
<span id="l390">        <span class="n">days</span><span class="p">,</span> <span class="n">seconds</span> <span class="o">=</span> <span class="nb">divmod</span><span class="p">(</span><span class="n">seconds</span><span class="p">,</span> <span class="mi">24</span><span class="o">*</span><span class="mi">3600</span><span class="p">)</span></span><a href="#l390"></a>
<span id="l391">        <span class="n">d</span> <span class="o">+=</span> <span class="n">days</span></span><a href="#l391"></a>
<span id="l392">        <span class="n">s</span> <span class="o">+=</span> <span class="nb">int</span><span class="p">(</span><span class="n">seconds</span><span class="p">)</span>    <span class="c"># can&#39;t overflow</span></span><a href="#l392"></a>
<span id="l393">        <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">s</span><span class="p">,</span> <span class="nb">int</span><span class="p">)</span></span><a href="#l393"></a>
<span id="l394">        <span class="k">assert</span> <span class="nb">abs</span><span class="p">(</span><span class="n">s</span><span class="p">)</span> <span class="o">&lt;=</span> <span class="mi">2</span> <span class="o">*</span> <span class="mi">24</span> <span class="o">*</span> <span class="mi">3600</span></span><a href="#l394"></a>
<span id="l395">        <span class="c"># seconds isn&#39;t referenced again before redefinition</span></span><a href="#l395"></a>
<span id="l396"></span><a href="#l396"></a>
<span id="l397">        <span class="n">usdouble</span> <span class="o">=</span> <span class="n">secondsfrac</span> <span class="o">*</span> <span class="mf">1e6</span></span><a href="#l397"></a>
<span id="l398">        <span class="k">assert</span> <span class="nb">abs</span><span class="p">(</span><span class="n">usdouble</span><span class="p">)</span> <span class="o">&lt;</span> <span class="mf">2.1e6</span>    <span class="c"># exact value not critical</span></span><a href="#l398"></a>
<span id="l399">        <span class="c"># secondsfrac isn&#39;t referenced again</span></span><a href="#l399"></a>
<span id="l400"></span><a href="#l400"></a>
<span id="l401">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">microseconds</span><span class="p">,</span> <span class="nb">float</span><span class="p">):</span></span><a href="#l401"></a>
<span id="l402">            <span class="n">microseconds</span> <span class="o">=</span> <span class="nb">round</span><span class="p">(</span><span class="n">microseconds</span> <span class="o">+</span> <span class="n">usdouble</span><span class="p">)</span></span><a href="#l402"></a>
<span id="l403">            <span class="n">seconds</span><span class="p">,</span> <span class="n">microseconds</span> <span class="o">=</span> <span class="nb">divmod</span><span class="p">(</span><span class="n">microseconds</span><span class="p">,</span> <span class="mi">1000000</span><span class="p">)</span></span><a href="#l403"></a>
<span id="l404">            <span class="n">days</span><span class="p">,</span> <span class="n">seconds</span> <span class="o">=</span> <span class="nb">divmod</span><span class="p">(</span><span class="n">seconds</span><span class="p">,</span> <span class="mi">24</span><span class="o">*</span><span class="mi">3600</span><span class="p">)</span></span><a href="#l404"></a>
<span id="l405">            <span class="n">d</span> <span class="o">+=</span> <span class="n">days</span></span><a href="#l405"></a>
<span id="l406">            <span class="n">s</span> <span class="o">+=</span> <span class="n">seconds</span></span><a href="#l406"></a>
<span id="l407">        <span class="k">else</span><span class="p">:</span></span><a href="#l407"></a>
<span id="l408">            <span class="n">microseconds</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">microseconds</span><span class="p">)</span></span><a href="#l408"></a>
<span id="l409">            <span class="n">seconds</span><span class="p">,</span> <span class="n">microseconds</span> <span class="o">=</span> <span class="nb">divmod</span><span class="p">(</span><span class="n">microseconds</span><span class="p">,</span> <span class="mi">1000000</span><span class="p">)</span></span><a href="#l409"></a>
<span id="l410">            <span class="n">days</span><span class="p">,</span> <span class="n">seconds</span> <span class="o">=</span> <span class="nb">divmod</span><span class="p">(</span><span class="n">seconds</span><span class="p">,</span> <span class="mi">24</span><span class="o">*</span><span class="mi">3600</span><span class="p">)</span></span><a href="#l410"></a>
<span id="l411">            <span class="n">d</span> <span class="o">+=</span> <span class="n">days</span></span><a href="#l411"></a>
<span id="l412">            <span class="n">s</span> <span class="o">+=</span> <span class="n">seconds</span></span><a href="#l412"></a>
<span id="l413">            <span class="n">microseconds</span> <span class="o">=</span> <span class="nb">round</span><span class="p">(</span><span class="n">microseconds</span> <span class="o">+</span> <span class="n">usdouble</span><span class="p">)</span></span><a href="#l413"></a>
<span id="l414">        <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">s</span><span class="p">,</span> <span class="nb">int</span><span class="p">)</span></span><a href="#l414"></a>
<span id="l415">        <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">microseconds</span><span class="p">,</span> <span class="nb">int</span><span class="p">)</span></span><a href="#l415"></a>
<span id="l416">        <span class="k">assert</span> <span class="nb">abs</span><span class="p">(</span><span class="n">s</span><span class="p">)</span> <span class="o">&lt;=</span> <span class="mi">3</span> <span class="o">*</span> <span class="mi">24</span> <span class="o">*</span> <span class="mi">3600</span></span><a href="#l416"></a>
<span id="l417">        <span class="k">assert</span> <span class="nb">abs</span><span class="p">(</span><span class="n">microseconds</span><span class="p">)</span> <span class="o">&lt;</span> <span class="mf">3.1e6</span></span><a href="#l417"></a>
<span id="l418"></span><a href="#l418"></a>
<span id="l419">        <span class="c"># Just a little bit of carrying possible for microseconds and seconds.</span></span><a href="#l419"></a>
<span id="l420">        <span class="n">seconds</span><span class="p">,</span> <span class="n">us</span> <span class="o">=</span> <span class="nb">divmod</span><span class="p">(</span><span class="n">microseconds</span><span class="p">,</span> <span class="mi">1000000</span><span class="p">)</span></span><a href="#l420"></a>
<span id="l421">        <span class="n">s</span> <span class="o">+=</span> <span class="n">seconds</span></span><a href="#l421"></a>
<span id="l422">        <span class="n">days</span><span class="p">,</span> <span class="n">s</span> <span class="o">=</span> <span class="nb">divmod</span><span class="p">(</span><span class="n">s</span><span class="p">,</span> <span class="mi">24</span><span class="o">*</span><span class="mi">3600</span><span class="p">)</span></span><a href="#l422"></a>
<span id="l423">        <span class="n">d</span> <span class="o">+=</span> <span class="n">days</span></span><a href="#l423"></a>
<span id="l424"></span><a href="#l424"></a>
<span id="l425">        <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">d</span><span class="p">,</span> <span class="nb">int</span><span class="p">)</span></span><a href="#l425"></a>
<span id="l426">        <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">s</span><span class="p">,</span> <span class="nb">int</span><span class="p">)</span> <span class="ow">and</span> <span class="mi">0</span> <span class="o">&lt;=</span> <span class="n">s</span> <span class="o">&lt;</span> <span class="mi">24</span><span class="o">*</span><span class="mi">3600</span></span><a href="#l426"></a>
<span id="l427">        <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">us</span><span class="p">,</span> <span class="nb">int</span><span class="p">)</span> <span class="ow">and</span> <span class="mi">0</span> <span class="o">&lt;=</span> <span class="n">us</span> <span class="o">&lt;</span> <span class="mi">1000000</span></span><a href="#l427"></a>
<span id="l428"></span><a href="#l428"></a>
<span id="l429">        <span class="k">if</span> <span class="nb">abs</span><span class="p">(</span><span class="n">d</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">999999999</span><span class="p">:</span></span><a href="#l429"></a>
<span id="l430">            <span class="k">raise</span> <span class="ne">OverflowError</span><span class="p">(</span><span class="s">&quot;timedelta # of days is too large: </span><span class="si">%d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="n">d</span><span class="p">)</span></span><a href="#l430"></a>
<span id="l431"></span><a href="#l431"></a>
<span id="l432">        <span class="bp">self</span> <span class="o">=</span> <span class="nb">object</span><span class="o">.</span><span class="n">__new__</span><span class="p">(</span><span class="n">cls</span><span class="p">)</span></span><a href="#l432"></a>
<span id="l433">        <span class="bp">self</span><span class="o">.</span><span class="n">_days</span> <span class="o">=</span> <span class="n">d</span></span><a href="#l433"></a>
<span id="l434">        <span class="bp">self</span><span class="o">.</span><span class="n">_seconds</span> <span class="o">=</span> <span class="n">s</span></span><a href="#l434"></a>
<span id="l435">        <span class="bp">self</span><span class="o">.</span><span class="n">_microseconds</span> <span class="o">=</span> <span class="n">us</span></span><a href="#l435"></a>
<span id="l436">        <span class="bp">self</span><span class="o">.</span><span class="n">_hashcode</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span></span><a href="#l436"></a>
<span id="l437">        <span class="k">return</span> <span class="bp">self</span></span><a href="#l437"></a>
<span id="l438"></span><a href="#l438"></a>
<span id="l439">    <span class="k">def</span> <span class="nf">__repr__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l439"></a>
<span id="l440">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_microseconds</span><span class="p">:</span></span><a href="#l440"></a>
<span id="l441">            <span class="k">return</span> <span class="s">&quot;</span><span class="si">%s</span><span class="s">.</span><span class="si">%s</span><span class="s">(</span><span class="si">%d</span><span class="s">, </span><span class="si">%d</span><span class="s">, </span><span class="si">%d</span><span class="s">)&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__class__</span><span class="o">.</span><span class="n">__module__</span><span class="p">,</span></span><a href="#l441"></a>
<span id="l442">                                          <span class="bp">self</span><span class="o">.</span><span class="n">__class__</span><span class="o">.</span><span class="n">__qualname__</span><span class="p">,</span></span><a href="#l442"></a>
<span id="l443">                                          <span class="bp">self</span><span class="o">.</span><span class="n">_days</span><span class="p">,</span></span><a href="#l443"></a>
<span id="l444">                                          <span class="bp">self</span><span class="o">.</span><span class="n">_seconds</span><span class="p">,</span></span><a href="#l444"></a>
<span id="l445">                                          <span class="bp">self</span><span class="o">.</span><span class="n">_microseconds</span><span class="p">)</span></span><a href="#l445"></a>
<span id="l446">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_seconds</span><span class="p">:</span></span><a href="#l446"></a>
<span id="l447">            <span class="k">return</span> <span class="s">&quot;</span><span class="si">%s</span><span class="s">.</span><span class="si">%s</span><span class="s">(</span><span class="si">%d</span><span class="s">, </span><span class="si">%d</span><span class="s">)&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__class__</span><span class="o">.</span><span class="n">__module__</span><span class="p">,</span></span><a href="#l447"></a>
<span id="l448">                                      <span class="bp">self</span><span class="o">.</span><span class="n">__class__</span><span class="o">.</span><span class="n">__qualname__</span><span class="p">,</span></span><a href="#l448"></a>
<span id="l449">                                      <span class="bp">self</span><span class="o">.</span><span class="n">_days</span><span class="p">,</span></span><a href="#l449"></a>
<span id="l450">                                      <span class="bp">self</span><span class="o">.</span><span class="n">_seconds</span><span class="p">)</span></span><a href="#l450"></a>
<span id="l451">        <span class="k">return</span> <span class="s">&quot;</span><span class="si">%s</span><span class="s">.</span><span class="si">%s</span><span class="s">(</span><span class="si">%d</span><span class="s">)&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__class__</span><span class="o">.</span><span class="n">__module__</span><span class="p">,</span></span><a href="#l451"></a>
<span id="l452">                              <span class="bp">self</span><span class="o">.</span><span class="n">__class__</span><span class="o">.</span><span class="n">__qualname__</span><span class="p">,</span></span><a href="#l452"></a>
<span id="l453">                              <span class="bp">self</span><span class="o">.</span><span class="n">_days</span><span class="p">)</span></span><a href="#l453"></a>
<span id="l454"></span><a href="#l454"></a>
<span id="l455">    <span class="k">def</span> <span class="nf">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l455"></a>
<span id="l456">        <span class="n">mm</span><span class="p">,</span> <span class="n">ss</span> <span class="o">=</span> <span class="nb">divmod</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_seconds</span><span class="p">,</span> <span class="mi">60</span><span class="p">)</span></span><a href="#l456"></a>
<span id="l457">        <span class="n">hh</span><span class="p">,</span> <span class="n">mm</span> <span class="o">=</span> <span class="nb">divmod</span><span class="p">(</span><span class="n">mm</span><span class="p">,</span> <span class="mi">60</span><span class="p">)</span></span><a href="#l457"></a>
<span id="l458">        <span class="n">s</span> <span class="o">=</span> <span class="s">&quot;</span><span class="si">%d</span><span class="s">:</span><span class="si">%02d</span><span class="s">:</span><span class="si">%02d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">hh</span><span class="p">,</span> <span class="n">mm</span><span class="p">,</span> <span class="n">ss</span><span class="p">)</span></span><a href="#l458"></a>
<span id="l459">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_days</span><span class="p">:</span></span><a href="#l459"></a>
<span id="l460">            <span class="k">def</span> <span class="nf">plural</span><span class="p">(</span><span class="n">n</span><span class="p">):</span></span><a href="#l460"></a>
<span id="l461">                <span class="k">return</span> <span class="n">n</span><span class="p">,</span> <span class="nb">abs</span><span class="p">(</span><span class="n">n</span><span class="p">)</span> <span class="o">!=</span> <span class="mi">1</span> <span class="ow">and</span> <span class="s">&quot;s&quot;</span> <span class="ow">or</span> <span class="s">&quot;&quot;</span></span><a href="#l461"></a>
<span id="l462">            <span class="n">s</span> <span class="o">=</span> <span class="p">(</span><span class="s">&quot;</span><span class="si">%d</span><span class="s"> day</span><span class="si">%s</span><span class="s">, &quot;</span> <span class="o">%</span> <span class="n">plural</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_days</span><span class="p">))</span> <span class="o">+</span> <span class="n">s</span></span><a href="#l462"></a>
<span id="l463">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_microseconds</span><span class="p">:</span></span><a href="#l463"></a>
<span id="l464">            <span class="n">s</span> <span class="o">=</span> <span class="n">s</span> <span class="o">+</span> <span class="s">&quot;.</span><span class="si">%06d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="bp">self</span><span class="o">.</span><span class="n">_microseconds</span></span><a href="#l464"></a>
<span id="l465">        <span class="k">return</span> <span class="n">s</span></span><a href="#l465"></a>
<span id="l466"></span><a href="#l466"></a>
<span id="l467">    <span class="k">def</span> <span class="nf">total_seconds</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l467"></a>
<span id="l468">        <span class="sd">&quot;&quot;&quot;Total seconds in the duration.&quot;&quot;&quot;</span></span><a href="#l468"></a>
<span id="l469">        <span class="k">return</span> <span class="p">((</span><span class="bp">self</span><span class="o">.</span><span class="n">days</span> <span class="o">*</span> <span class="mi">86400</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">seconds</span><span class="p">)</span> <span class="o">*</span> <span class="mi">10</span><span class="o">**</span><span class="mi">6</span> <span class="o">+</span></span><a href="#l469"></a>
<span id="l470">                <span class="bp">self</span><span class="o">.</span><span class="n">microseconds</span><span class="p">)</span> <span class="o">/</span> <span class="mi">10</span><span class="o">**</span><span class="mi">6</span></span><a href="#l470"></a>
<span id="l471"></span><a href="#l471"></a>
<span id="l472">    <span class="c"># Read-only field accessors</span></span><a href="#l472"></a>
<span id="l473">    <span class="nd">@property</span></span><a href="#l473"></a>
<span id="l474">    <span class="k">def</span> <span class="nf">days</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l474"></a>
<span id="l475">        <span class="sd">&quot;&quot;&quot;days&quot;&quot;&quot;</span></span><a href="#l475"></a>
<span id="l476">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_days</span></span><a href="#l476"></a>
<span id="l477"></span><a href="#l477"></a>
<span id="l478">    <span class="nd">@property</span></span><a href="#l478"></a>
<span id="l479">    <span class="k">def</span> <span class="nf">seconds</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l479"></a>
<span id="l480">        <span class="sd">&quot;&quot;&quot;seconds&quot;&quot;&quot;</span></span><a href="#l480"></a>
<span id="l481">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_seconds</span></span><a href="#l481"></a>
<span id="l482"></span><a href="#l482"></a>
<span id="l483">    <span class="nd">@property</span></span><a href="#l483"></a>
<span id="l484">    <span class="k">def</span> <span class="nf">microseconds</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l484"></a>
<span id="l485">        <span class="sd">&quot;&quot;&quot;microseconds&quot;&quot;&quot;</span></span><a href="#l485"></a>
<span id="l486">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_microseconds</span></span><a href="#l486"></a>
<span id="l487"></span><a href="#l487"></a>
<span id="l488">    <span class="k">def</span> <span class="nf">__add__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l488"></a>
<span id="l489">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">timedelta</span><span class="p">):</span></span><a href="#l489"></a>
<span id="l490">            <span class="c"># for CPython compatibility, we cannot use</span></span><a href="#l490"></a>
<span id="l491">            <span class="c"># our __class__ here, but need a real timedelta</span></span><a href="#l491"></a>
<span id="l492">            <span class="k">return</span> <span class="n">timedelta</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_days</span> <span class="o">+</span> <span class="n">other</span><span class="o">.</span><span class="n">_days</span><span class="p">,</span></span><a href="#l492"></a>
<span id="l493">                             <span class="bp">self</span><span class="o">.</span><span class="n">_seconds</span> <span class="o">+</span> <span class="n">other</span><span class="o">.</span><span class="n">_seconds</span><span class="p">,</span></span><a href="#l493"></a>
<span id="l494">                             <span class="bp">self</span><span class="o">.</span><span class="n">_microseconds</span> <span class="o">+</span> <span class="n">other</span><span class="o">.</span><span class="n">_microseconds</span><span class="p">)</span></span><a href="#l494"></a>
<span id="l495">        <span class="k">return</span> <span class="bp">NotImplemented</span></span><a href="#l495"></a>
<span id="l496"></span><a href="#l496"></a>
<span id="l497">    <span class="n">__radd__</span> <span class="o">=</span> <span class="n">__add__</span></span><a href="#l497"></a>
<span id="l498"></span><a href="#l498"></a>
<span id="l499">    <span class="k">def</span> <span class="nf">__sub__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l499"></a>
<span id="l500">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">timedelta</span><span class="p">):</span></span><a href="#l500"></a>
<span id="l501">            <span class="c"># for CPython compatibility, we cannot use</span></span><a href="#l501"></a>
<span id="l502">            <span class="c"># our __class__ here, but need a real timedelta</span></span><a href="#l502"></a>
<span id="l503">            <span class="k">return</span> <span class="n">timedelta</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_days</span> <span class="o">-</span> <span class="n">other</span><span class="o">.</span><span class="n">_days</span><span class="p">,</span></span><a href="#l503"></a>
<span id="l504">                             <span class="bp">self</span><span class="o">.</span><span class="n">_seconds</span> <span class="o">-</span> <span class="n">other</span><span class="o">.</span><span class="n">_seconds</span><span class="p">,</span></span><a href="#l504"></a>
<span id="l505">                             <span class="bp">self</span><span class="o">.</span><span class="n">_microseconds</span> <span class="o">-</span> <span class="n">other</span><span class="o">.</span><span class="n">_microseconds</span><span class="p">)</span></span><a href="#l505"></a>
<span id="l506">        <span class="k">return</span> <span class="bp">NotImplemented</span></span><a href="#l506"></a>
<span id="l507"></span><a href="#l507"></a>
<span id="l508">    <span class="k">def</span> <span class="nf">__rsub__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l508"></a>
<span id="l509">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">timedelta</span><span class="p">):</span></span><a href="#l509"></a>
<span id="l510">            <span class="k">return</span> <span class="o">-</span><span class="bp">self</span> <span class="o">+</span> <span class="n">other</span></span><a href="#l510"></a>
<span id="l511">        <span class="k">return</span> <span class="bp">NotImplemented</span></span><a href="#l511"></a>
<span id="l512"></span><a href="#l512"></a>
<span id="l513">    <span class="k">def</span> <span class="nf">__neg__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l513"></a>
<span id="l514">        <span class="c"># for CPython compatibility, we cannot use</span></span><a href="#l514"></a>
<span id="l515">        <span class="c"># our __class__ here, but need a real timedelta</span></span><a href="#l515"></a>
<span id="l516">        <span class="k">return</span> <span class="n">timedelta</span><span class="p">(</span><span class="o">-</span><span class="bp">self</span><span class="o">.</span><span class="n">_days</span><span class="p">,</span></span><a href="#l516"></a>
<span id="l517">                         <span class="o">-</span><span class="bp">self</span><span class="o">.</span><span class="n">_seconds</span><span class="p">,</span></span><a href="#l517"></a>
<span id="l518">                         <span class="o">-</span><span class="bp">self</span><span class="o">.</span><span class="n">_microseconds</span><span class="p">)</span></span><a href="#l518"></a>
<span id="l519"></span><a href="#l519"></a>
<span id="l520">    <span class="k">def</span> <span class="nf">__pos__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l520"></a>
<span id="l521">        <span class="k">return</span> <span class="bp">self</span></span><a href="#l521"></a>
<span id="l522"></span><a href="#l522"></a>
<span id="l523">    <span class="k">def</span> <span class="nf">__abs__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l523"></a>
<span id="l524">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_days</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span></span><a href="#l524"></a>
<span id="l525">            <span class="k">return</span> <span class="o">-</span><span class="bp">self</span></span><a href="#l525"></a>
<span id="l526">        <span class="k">else</span><span class="p">:</span></span><a href="#l526"></a>
<span id="l527">            <span class="k">return</span> <span class="bp">self</span></span><a href="#l527"></a>
<span id="l528"></span><a href="#l528"></a>
<span id="l529">    <span class="k">def</span> <span class="nf">__mul__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l529"></a>
<span id="l530">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="nb">int</span><span class="p">):</span></span><a href="#l530"></a>
<span id="l531">            <span class="c"># for CPython compatibility, we cannot use</span></span><a href="#l531"></a>
<span id="l532">            <span class="c"># our __class__ here, but need a real timedelta</span></span><a href="#l532"></a>
<span id="l533">            <span class="k">return</span> <span class="n">timedelta</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_days</span> <span class="o">*</span> <span class="n">other</span><span class="p">,</span></span><a href="#l533"></a>
<span id="l534">                             <span class="bp">self</span><span class="o">.</span><span class="n">_seconds</span> <span class="o">*</span> <span class="n">other</span><span class="p">,</span></span><a href="#l534"></a>
<span id="l535">                             <span class="bp">self</span><span class="o">.</span><span class="n">_microseconds</span> <span class="o">*</span> <span class="n">other</span><span class="p">)</span></span><a href="#l535"></a>
<span id="l536">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="nb">float</span><span class="p">):</span></span><a href="#l536"></a>
<span id="l537">            <span class="n">usec</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_to_microseconds</span><span class="p">()</span></span><a href="#l537"></a>
<span id="l538">            <span class="n">a</span><span class="p">,</span> <span class="n">b</span> <span class="o">=</span> <span class="n">other</span><span class="o">.</span><span class="n">as_integer_ratio</span><span class="p">()</span></span><a href="#l538"></a>
<span id="l539">            <span class="k">return</span> <span class="n">timedelta</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="n">_divide_and_round</span><span class="p">(</span><span class="n">usec</span> <span class="o">*</span> <span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">))</span></span><a href="#l539"></a>
<span id="l540">        <span class="k">return</span> <span class="bp">NotImplemented</span></span><a href="#l540"></a>
<span id="l541"></span><a href="#l541"></a>
<span id="l542">    <span class="n">__rmul__</span> <span class="o">=</span> <span class="n">__mul__</span></span><a href="#l542"></a>
<span id="l543"></span><a href="#l543"></a>
<span id="l544">    <span class="k">def</span> <span class="nf">_to_microseconds</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l544"></a>
<span id="l545">        <span class="k">return</span> <span class="p">((</span><span class="bp">self</span><span class="o">.</span><span class="n">_days</span> <span class="o">*</span> <span class="p">(</span><span class="mi">24</span><span class="o">*</span><span class="mi">3600</span><span class="p">)</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">_seconds</span><span class="p">)</span> <span class="o">*</span> <span class="mi">1000000</span> <span class="o">+</span></span><a href="#l545"></a>
<span id="l546">                <span class="bp">self</span><span class="o">.</span><span class="n">_microseconds</span><span class="p">)</span></span><a href="#l546"></a>
<span id="l547"></span><a href="#l547"></a>
<span id="l548">    <span class="k">def</span> <span class="nf">__floordiv__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l548"></a>
<span id="l549">        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="p">(</span><span class="nb">int</span><span class="p">,</span> <span class="n">timedelta</span><span class="p">)):</span></span><a href="#l549"></a>
<span id="l550">            <span class="k">return</span> <span class="bp">NotImplemented</span></span><a href="#l550"></a>
<span id="l551">        <span class="n">usec</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_to_microseconds</span><span class="p">()</span></span><a href="#l551"></a>
<span id="l552">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">timedelta</span><span class="p">):</span></span><a href="#l552"></a>
<span id="l553">            <span class="k">return</span> <span class="n">usec</span> <span class="o">//</span> <span class="n">other</span><span class="o">.</span><span class="n">_to_microseconds</span><span class="p">()</span></span><a href="#l553"></a>
<span id="l554">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="nb">int</span><span class="p">):</span></span><a href="#l554"></a>
<span id="l555">            <span class="k">return</span> <span class="n">timedelta</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="n">usec</span> <span class="o">//</span> <span class="n">other</span><span class="p">)</span></span><a href="#l555"></a>
<span id="l556"></span><a href="#l556"></a>
<span id="l557">    <span class="k">def</span> <span class="nf">__truediv__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l557"></a>
<span id="l558">        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="p">(</span><span class="nb">int</span><span class="p">,</span> <span class="nb">float</span><span class="p">,</span> <span class="n">timedelta</span><span class="p">)):</span></span><a href="#l558"></a>
<span id="l559">            <span class="k">return</span> <span class="bp">NotImplemented</span></span><a href="#l559"></a>
<span id="l560">        <span class="n">usec</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_to_microseconds</span><span class="p">()</span></span><a href="#l560"></a>
<span id="l561">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">timedelta</span><span class="p">):</span></span><a href="#l561"></a>
<span id="l562">            <span class="k">return</span> <span class="n">usec</span> <span class="o">/</span> <span class="n">other</span><span class="o">.</span><span class="n">_to_microseconds</span><span class="p">()</span></span><a href="#l562"></a>
<span id="l563">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="nb">int</span><span class="p">):</span></span><a href="#l563"></a>
<span id="l564">            <span class="k">return</span> <span class="n">timedelta</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="n">_divide_and_round</span><span class="p">(</span><span class="n">usec</span><span class="p">,</span> <span class="n">other</span><span class="p">))</span></span><a href="#l564"></a>
<span id="l565">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="nb">float</span><span class="p">):</span></span><a href="#l565"></a>
<span id="l566">            <span class="n">a</span><span class="p">,</span> <span class="n">b</span> <span class="o">=</span> <span class="n">other</span><span class="o">.</span><span class="n">as_integer_ratio</span><span class="p">()</span></span><a href="#l566"></a>
<span id="l567">            <span class="k">return</span> <span class="n">timedelta</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="n">_divide_and_round</span><span class="p">(</span><span class="n">b</span> <span class="o">*</span> <span class="n">usec</span><span class="p">,</span> <span class="n">a</span><span class="p">))</span></span><a href="#l567"></a>
<span id="l568"></span><a href="#l568"></a>
<span id="l569">    <span class="k">def</span> <span class="nf">__mod__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l569"></a>
<span id="l570">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">timedelta</span><span class="p">):</span></span><a href="#l570"></a>
<span id="l571">            <span class="n">r</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_to_microseconds</span><span class="p">()</span> <span class="o">%</span> <span class="n">other</span><span class="o">.</span><span class="n">_to_microseconds</span><span class="p">()</span></span><a href="#l571"></a>
<span id="l572">            <span class="k">return</span> <span class="n">timedelta</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="n">r</span><span class="p">)</span></span><a href="#l572"></a>
<span id="l573">        <span class="k">return</span> <span class="bp">NotImplemented</span></span><a href="#l573"></a>
<span id="l574"></span><a href="#l574"></a>
<span id="l575">    <span class="k">def</span> <span class="nf">__divmod__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l575"></a>
<span id="l576">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">timedelta</span><span class="p">):</span></span><a href="#l576"></a>
<span id="l577">            <span class="n">q</span><span class="p">,</span> <span class="n">r</span> <span class="o">=</span> <span class="nb">divmod</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_to_microseconds</span><span class="p">(),</span></span><a href="#l577"></a>
<span id="l578">                          <span class="n">other</span><span class="o">.</span><span class="n">_to_microseconds</span><span class="p">())</span></span><a href="#l578"></a>
<span id="l579">            <span class="k">return</span> <span class="n">q</span><span class="p">,</span> <span class="n">timedelta</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="n">r</span><span class="p">)</span></span><a href="#l579"></a>
<span id="l580">        <span class="k">return</span> <span class="bp">NotImplemented</span></span><a href="#l580"></a>
<span id="l581"></span><a href="#l581"></a>
<span id="l582">    <span class="c"># Comparisons of timedelta objects with other.</span></span><a href="#l582"></a>
<span id="l583"></span><a href="#l583"></a>
<span id="l584">    <span class="k">def</span> <span class="nf">__eq__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l584"></a>
<span id="l585">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">timedelta</span><span class="p">):</span></span><a href="#l585"></a>
<span id="l586">            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cmp</span><span class="p">(</span><span class="n">other</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span></span><a href="#l586"></a>
<span id="l587">        <span class="k">else</span><span class="p">:</span></span><a href="#l587"></a>
<span id="l588">            <span class="k">return</span> <span class="bp">False</span></span><a href="#l588"></a>
<span id="l589"></span><a href="#l589"></a>
<span id="l590">    <span class="k">def</span> <span class="nf">__le__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l590"></a>
<span id="l591">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">timedelta</span><span class="p">):</span></span><a href="#l591"></a>
<span id="l592">            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cmp</span><span class="p">(</span><span class="n">other</span><span class="p">)</span> <span class="o">&lt;=</span> <span class="mi">0</span></span><a href="#l592"></a>
<span id="l593">        <span class="k">else</span><span class="p">:</span></span><a href="#l593"></a>
<span id="l594">            <span class="n">_cmperror</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">)</span></span><a href="#l594"></a>
<span id="l595"></span><a href="#l595"></a>
<span id="l596">    <span class="k">def</span> <span class="nf">__lt__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l596"></a>
<span id="l597">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">timedelta</span><span class="p">):</span></span><a href="#l597"></a>
<span id="l598">            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cmp</span><span class="p">(</span><span class="n">other</span><span class="p">)</span> <span class="o">&lt;</span> <span class="mi">0</span></span><a href="#l598"></a>
<span id="l599">        <span class="k">else</span><span class="p">:</span></span><a href="#l599"></a>
<span id="l600">            <span class="n">_cmperror</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">)</span></span><a href="#l600"></a>
<span id="l601"></span><a href="#l601"></a>
<span id="l602">    <span class="k">def</span> <span class="nf">__ge__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l602"></a>
<span id="l603">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">timedelta</span><span class="p">):</span></span><a href="#l603"></a>
<span id="l604">            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cmp</span><span class="p">(</span><span class="n">other</span><span class="p">)</span> <span class="o">&gt;=</span> <span class="mi">0</span></span><a href="#l604"></a>
<span id="l605">        <span class="k">else</span><span class="p">:</span></span><a href="#l605"></a>
<span id="l606">            <span class="n">_cmperror</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">)</span></span><a href="#l606"></a>
<span id="l607"></span><a href="#l607"></a>
<span id="l608">    <span class="k">def</span> <span class="nf">__gt__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l608"></a>
<span id="l609">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">timedelta</span><span class="p">):</span></span><a href="#l609"></a>
<span id="l610">            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cmp</span><span class="p">(</span><span class="n">other</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span></span><a href="#l610"></a>
<span id="l611">        <span class="k">else</span><span class="p">:</span></span><a href="#l611"></a>
<span id="l612">            <span class="n">_cmperror</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">)</span></span><a href="#l612"></a>
<span id="l613"></span><a href="#l613"></a>
<span id="l614">    <span class="k">def</span> <span class="nf">_cmp</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l614"></a>
<span id="l615">        <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">timedelta</span><span class="p">)</span></span><a href="#l615"></a>
<span id="l616">        <span class="k">return</span> <span class="n">_cmp</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_getstate</span><span class="p">(),</span> <span class="n">other</span><span class="o">.</span><span class="n">_getstate</span><span class="p">())</span></span><a href="#l616"></a>
<span id="l617"></span><a href="#l617"></a>
<span id="l618">    <span class="k">def</span> <span class="nf">__hash__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l618"></a>
<span id="l619">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_hashcode</span> <span class="o">==</span> <span class="o">-</span><span class="mi">1</span><span class="p">:</span></span><a href="#l619"></a>
<span id="l620">            <span class="bp">self</span><span class="o">.</span><span class="n">_hashcode</span> <span class="o">=</span> <span class="nb">hash</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_getstate</span><span class="p">())</span></span><a href="#l620"></a>
<span id="l621">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_hashcode</span></span><a href="#l621"></a>
<span id="l622"></span><a href="#l622"></a>
<span id="l623">    <span class="k">def</span> <span class="nf">__bool__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l623"></a>
<span id="l624">        <span class="k">return</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_days</span> <span class="o">!=</span> <span class="mi">0</span> <span class="ow">or</span></span><a href="#l624"></a>
<span id="l625">                <span class="bp">self</span><span class="o">.</span><span class="n">_seconds</span> <span class="o">!=</span> <span class="mi">0</span> <span class="ow">or</span></span><a href="#l625"></a>
<span id="l626">                <span class="bp">self</span><span class="o">.</span><span class="n">_microseconds</span> <span class="o">!=</span> <span class="mi">0</span><span class="p">)</span></span><a href="#l626"></a>
<span id="l627"></span><a href="#l627"></a>
<span id="l628">    <span class="c"># Pickle support.</span></span><a href="#l628"></a>
<span id="l629"></span><a href="#l629"></a>
<span id="l630">    <span class="k">def</span> <span class="nf">_getstate</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l630"></a>
<span id="l631">        <span class="k">return</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_days</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_seconds</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_microseconds</span><span class="p">)</span></span><a href="#l631"></a>
<span id="l632"></span><a href="#l632"></a>
<span id="l633">    <span class="k">def</span> <span class="nf">__reduce__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l633"></a>
<span id="l634">        <span class="k">return</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__class__</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_getstate</span><span class="p">())</span></span><a href="#l634"></a>
<span id="l635"></span><a href="#l635"></a>
<span id="l636"><span class="n">timedelta</span><span class="o">.</span><span class="n">min</span> <span class="o">=</span> <span class="n">timedelta</span><span class="p">(</span><span class="o">-</span><span class="mi">999999999</span><span class="p">)</span></span><a href="#l636"></a>
<span id="l637"><span class="n">timedelta</span><span class="o">.</span><span class="n">max</span> <span class="o">=</span> <span class="n">timedelta</span><span class="p">(</span><span class="n">days</span><span class="o">=</span><span class="mi">999999999</span><span class="p">,</span> <span class="n">hours</span><span class="o">=</span><span class="mi">23</span><span class="p">,</span> <span class="n">minutes</span><span class="o">=</span><span class="mi">59</span><span class="p">,</span> <span class="n">seconds</span><span class="o">=</span><span class="mi">59</span><span class="p">,</span></span><a href="#l637"></a>
<span id="l638">                          <span class="n">microseconds</span><span class="o">=</span><span class="mi">999999</span><span class="p">)</span></span><a href="#l638"></a>
<span id="l639"><span class="n">timedelta</span><span class="o">.</span><span class="n">resolution</span> <span class="o">=</span> <span class="n">timedelta</span><span class="p">(</span><span class="n">microseconds</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span></span><a href="#l639"></a>
<span id="l640"></span><a href="#l640"></a>
<span id="l641"><span class="k">class</span> <span class="nc">date</span><span class="p">:</span></span><a href="#l641"></a>
<span id="l642">    <span class="sd">&quot;&quot;&quot;Concrete date type.</span></span><a href="#l642"></a>
<span id="l643"></span><a href="#l643"></a>
<span id="l644"><span class="sd">    Constructors:</span></span><a href="#l644"></a>
<span id="l645"></span><a href="#l645"></a>
<span id="l646"><span class="sd">    __new__()</span></span><a href="#l646"></a>
<span id="l647"><span class="sd">    fromtimestamp()</span></span><a href="#l647"></a>
<span id="l648"><span class="sd">    today()</span></span><a href="#l648"></a>
<span id="l649"><span class="sd">    fromordinal()</span></span><a href="#l649"></a>
<span id="l650"></span><a href="#l650"></a>
<span id="l651"><span class="sd">    Operators:</span></span><a href="#l651"></a>
<span id="l652"></span><a href="#l652"></a>
<span id="l653"><span class="sd">    __repr__, __str__</span></span><a href="#l653"></a>
<span id="l654"><span class="sd">    __eq__, __le__, __lt__, __ge__, __gt__, __hash__</span></span><a href="#l654"></a>
<span id="l655"><span class="sd">    __add__, __radd__, __sub__ (add/radd only with timedelta arg)</span></span><a href="#l655"></a>
<span id="l656"></span><a href="#l656"></a>
<span id="l657"><span class="sd">    Methods:</span></span><a href="#l657"></a>
<span id="l658"></span><a href="#l658"></a>
<span id="l659"><span class="sd">    timetuple()</span></span><a href="#l659"></a>
<span id="l660"><span class="sd">    toordinal()</span></span><a href="#l660"></a>
<span id="l661"><span class="sd">    weekday()</span></span><a href="#l661"></a>
<span id="l662"><span class="sd">    isoweekday(), isocalendar(), isoformat()</span></span><a href="#l662"></a>
<span id="l663"><span class="sd">    ctime()</span></span><a href="#l663"></a>
<span id="l664"><span class="sd">    strftime()</span></span><a href="#l664"></a>
<span id="l665"></span><a href="#l665"></a>
<span id="l666"><span class="sd">    Properties (readonly):</span></span><a href="#l666"></a>
<span id="l667"><span class="sd">    year, month, day</span></span><a href="#l667"></a>
<span id="l668"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l668"></a>
<span id="l669">    <span class="n">__slots__</span> <span class="o">=</span> <span class="s">&#39;_year&#39;</span><span class="p">,</span> <span class="s">&#39;_month&#39;</span><span class="p">,</span> <span class="s">&#39;_day&#39;</span><span class="p">,</span> <span class="s">&#39;_hashcode&#39;</span></span><a href="#l669"></a>
<span id="l670"></span><a href="#l670"></a>
<span id="l671">    <span class="k">def</span> <span class="nf">__new__</span><span class="p">(</span><span class="n">cls</span><span class="p">,</span> <span class="n">year</span><span class="p">,</span> <span class="n">month</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">day</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l671"></a>
<span id="l672">        <span class="sd">&quot;&quot;&quot;Constructor.</span></span><a href="#l672"></a>
<span id="l673"></span><a href="#l673"></a>
<span id="l674"><span class="sd">        Arguments:</span></span><a href="#l674"></a>
<span id="l675"></span><a href="#l675"></a>
<span id="l676"><span class="sd">        year, month, day (required, base 1)</span></span><a href="#l676"></a>
<span id="l677"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l677"></a>
<span id="l678">        <span class="k">if</span> <span class="n">month</span> <span class="ow">is</span> <span class="bp">None</span> <span class="ow">and</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">year</span><span class="p">,</span> <span class="nb">bytes</span><span class="p">)</span> <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="n">year</span><span class="p">)</span> <span class="o">==</span> <span class="mi">4</span> <span class="ow">and</span> \</span><a href="#l678"></a>
<span id="l679">                <span class="mi">1</span> <span class="o">&lt;=</span> <span class="n">year</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span> <span class="o">&lt;=</span> <span class="mi">12</span><span class="p">:</span></span><a href="#l679"></a>
<span id="l680">            <span class="c"># Pickle support</span></span><a href="#l680"></a>
<span id="l681">            <span class="bp">self</span> <span class="o">=</span> <span class="nb">object</span><span class="o">.</span><span class="n">__new__</span><span class="p">(</span><span class="n">cls</span><span class="p">)</span></span><a href="#l681"></a>
<span id="l682">            <span class="bp">self</span><span class="o">.</span><span class="n">__setstate</span><span class="p">(</span><span class="n">year</span><span class="p">)</span></span><a href="#l682"></a>
<span id="l683">            <span class="bp">self</span><span class="o">.</span><span class="n">_hashcode</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span></span><a href="#l683"></a>
<span id="l684">            <span class="k">return</span> <span class="bp">self</span></span><a href="#l684"></a>
<span id="l685">        <span class="n">year</span><span class="p">,</span> <span class="n">month</span><span class="p">,</span> <span class="n">day</span> <span class="o">=</span> <span class="n">_check_date_fields</span><span class="p">(</span><span class="n">year</span><span class="p">,</span> <span class="n">month</span><span class="p">,</span> <span class="n">day</span><span class="p">)</span></span><a href="#l685"></a>
<span id="l686">        <span class="bp">self</span> <span class="o">=</span> <span class="nb">object</span><span class="o">.</span><span class="n">__new__</span><span class="p">(</span><span class="n">cls</span><span class="p">)</span></span><a href="#l686"></a>
<span id="l687">        <span class="bp">self</span><span class="o">.</span><span class="n">_year</span> <span class="o">=</span> <span class="n">year</span></span><a href="#l687"></a>
<span id="l688">        <span class="bp">self</span><span class="o">.</span><span class="n">_month</span> <span class="o">=</span> <span class="n">month</span></span><a href="#l688"></a>
<span id="l689">        <span class="bp">self</span><span class="o">.</span><span class="n">_day</span> <span class="o">=</span> <span class="n">day</span></span><a href="#l689"></a>
<span id="l690">        <span class="bp">self</span><span class="o">.</span><span class="n">_hashcode</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span></span><a href="#l690"></a>
<span id="l691">        <span class="k">return</span> <span class="bp">self</span></span><a href="#l691"></a>
<span id="l692"></span><a href="#l692"></a>
<span id="l693">    <span class="c"># Additional constructors</span></span><a href="#l693"></a>
<span id="l694"></span><a href="#l694"></a>
<span id="l695">    <span class="nd">@classmethod</span></span><a href="#l695"></a>
<span id="l696">    <span class="k">def</span> <span class="nf">fromtimestamp</span><span class="p">(</span><span class="n">cls</span><span class="p">,</span> <span class="n">t</span><span class="p">):</span></span><a href="#l696"></a>
<span id="l697">        <span class="s">&quot;Construct a date from a POSIX timestamp (like time.time()).&quot;</span></span><a href="#l697"></a>
<span id="l698">        <span class="n">y</span><span class="p">,</span> <span class="n">m</span><span class="p">,</span> <span class="n">d</span><span class="p">,</span> <span class="n">hh</span><span class="p">,</span> <span class="n">mm</span><span class="p">,</span> <span class="n">ss</span><span class="p">,</span> <span class="n">weekday</span><span class="p">,</span> <span class="n">jday</span><span class="p">,</span> <span class="n">dst</span> <span class="o">=</span> <span class="n">_time</span><span class="o">.</span><span class="n">localtime</span><span class="p">(</span><span class="n">t</span><span class="p">)</span></span><a href="#l698"></a>
<span id="l699">        <span class="k">return</span> <span class="n">cls</span><span class="p">(</span><span class="n">y</span><span class="p">,</span> <span class="n">m</span><span class="p">,</span> <span class="n">d</span><span class="p">)</span></span><a href="#l699"></a>
<span id="l700"></span><a href="#l700"></a>
<span id="l701">    <span class="nd">@classmethod</span></span><a href="#l701"></a>
<span id="l702">    <span class="k">def</span> <span class="nf">today</span><span class="p">(</span><span class="n">cls</span><span class="p">):</span></span><a href="#l702"></a>
<span id="l703">        <span class="s">&quot;Construct a date from time.time().&quot;</span></span><a href="#l703"></a>
<span id="l704">        <span class="n">t</span> <span class="o">=</span> <span class="n">_time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span></span><a href="#l704"></a>
<span id="l705">        <span class="k">return</span> <span class="n">cls</span><span class="o">.</span><span class="n">fromtimestamp</span><span class="p">(</span><span class="n">t</span><span class="p">)</span></span><a href="#l705"></a>
<span id="l706"></span><a href="#l706"></a>
<span id="l707">    <span class="nd">@classmethod</span></span><a href="#l707"></a>
<span id="l708">    <span class="k">def</span> <span class="nf">fromordinal</span><span class="p">(</span><span class="n">cls</span><span class="p">,</span> <span class="n">n</span><span class="p">):</span></span><a href="#l708"></a>
<span id="l709">        <span class="sd">&quot;&quot;&quot;Construct a date from a proleptic Gregorian ordinal.</span></span><a href="#l709"></a>
<span id="l710"></span><a href="#l710"></a>
<span id="l711"><span class="sd">        January 1 of year 1 is day 1.  Only the year, month and day are</span></span><a href="#l711"></a>
<span id="l712"><span class="sd">        non-zero in the result.</span></span><a href="#l712"></a>
<span id="l713"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l713"></a>
<span id="l714">        <span class="n">y</span><span class="p">,</span> <span class="n">m</span><span class="p">,</span> <span class="n">d</span> <span class="o">=</span> <span class="n">_ord2ymd</span><span class="p">(</span><span class="n">n</span><span class="p">)</span></span><a href="#l714"></a>
<span id="l715">        <span class="k">return</span> <span class="n">cls</span><span class="p">(</span><span class="n">y</span><span class="p">,</span> <span class="n">m</span><span class="p">,</span> <span class="n">d</span><span class="p">)</span></span><a href="#l715"></a>
<span id="l716"></span><a href="#l716"></a>
<span id="l717">    <span class="c"># Conversions to string</span></span><a href="#l717"></a>
<span id="l718"></span><a href="#l718"></a>
<span id="l719">    <span class="k">def</span> <span class="nf">__repr__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l719"></a>
<span id="l720">        <span class="sd">&quot;&quot;&quot;Convert to formal string, for repr().</span></span><a href="#l720"></a>
<span id="l721"></span><a href="#l721"></a>
<span id="l722"><span class="sd">        &gt;&gt;&gt; dt = datetime(2010, 1, 1)</span></span><a href="#l722"></a>
<span id="l723"><span class="sd">        &gt;&gt;&gt; repr(dt)</span></span><a href="#l723"></a>
<span id="l724"><span class="sd">        &#39;datetime.datetime(2010, 1, 1, 0, 0)&#39;</span></span><a href="#l724"></a>
<span id="l725"></span><a href="#l725"></a>
<span id="l726"><span class="sd">        &gt;&gt;&gt; dt = datetime(2010, 1, 1, tzinfo=timezone.utc)</span></span><a href="#l726"></a>
<span id="l727"><span class="sd">        &gt;&gt;&gt; repr(dt)</span></span><a href="#l727"></a>
<span id="l728"><span class="sd">        &#39;datetime.datetime(2010, 1, 1, 0, 0, tzinfo=datetime.timezone.utc)&#39;</span></span><a href="#l728"></a>
<span id="l729"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l729"></a>
<span id="l730">        <span class="k">return</span> <span class="s">&quot;</span><span class="si">%s</span><span class="s">.</span><span class="si">%s</span><span class="s">(</span><span class="si">%d</span><span class="s">, </span><span class="si">%d</span><span class="s">, </span><span class="si">%d</span><span class="s">)&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__class__</span><span class="o">.</span><span class="n">__module__</span><span class="p">,</span></span><a href="#l730"></a>
<span id="l731">                                      <span class="bp">self</span><span class="o">.</span><span class="n">__class__</span><span class="o">.</span><span class="n">__qualname__</span><span class="p">,</span></span><a href="#l731"></a>
<span id="l732">                                      <span class="bp">self</span><span class="o">.</span><span class="n">_year</span><span class="p">,</span></span><a href="#l732"></a>
<span id="l733">                                      <span class="bp">self</span><span class="o">.</span><span class="n">_month</span><span class="p">,</span></span><a href="#l733"></a>
<span id="l734">                                      <span class="bp">self</span><span class="o">.</span><span class="n">_day</span><span class="p">)</span></span><a href="#l734"></a>
<span id="l735">    <span class="c"># XXX These shouldn&#39;t depend on time.localtime(), because that</span></span><a href="#l735"></a>
<span id="l736">    <span class="c"># clips the usable dates to [1970 .. 2038).  At least ctime() is</span></span><a href="#l736"></a>
<span id="l737">    <span class="c"># easily done without using strftime() -- that&#39;s better too because</span></span><a href="#l737"></a>
<span id="l738">    <span class="c"># strftime(&quot;%c&quot;, ...) is locale specific.</span></span><a href="#l738"></a>
<span id="l739"></span><a href="#l739"></a>
<span id="l740"></span><a href="#l740"></a>
<span id="l741">    <span class="k">def</span> <span class="nf">ctime</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l741"></a>
<span id="l742">        <span class="s">&quot;Return ctime() style string.&quot;</span></span><a href="#l742"></a>
<span id="l743">        <span class="n">weekday</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">toordinal</span><span class="p">()</span> <span class="o">%</span> <span class="mi">7</span> <span class="ow">or</span> <span class="mi">7</span></span><a href="#l743"></a>
<span id="l744">        <span class="k">return</span> <span class="s">&quot;</span><span class="si">%s</span><span class="s"> </span><span class="si">%s</span><span class="s"> </span><span class="si">%2d</span><span class="s"> 00:00:00 </span><span class="si">%04d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span></span><a href="#l744"></a>
<span id="l745">            <span class="n">_DAYNAMES</span><span class="p">[</span><span class="n">weekday</span><span class="p">],</span></span><a href="#l745"></a>
<span id="l746">            <span class="n">_MONTHNAMES</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_month</span><span class="p">],</span></span><a href="#l746"></a>
<span id="l747">            <span class="bp">self</span><span class="o">.</span><span class="n">_day</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_year</span><span class="p">)</span></span><a href="#l747"></a>
<span id="l748"></span><a href="#l748"></a>
<span id="l749">    <span class="k">def</span> <span class="nf">strftime</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fmt</span><span class="p">):</span></span><a href="#l749"></a>
<span id="l750">        <span class="s">&quot;Format using strftime().&quot;</span></span><a href="#l750"></a>
<span id="l751">        <span class="k">return</span> <span class="n">_wrap_strftime</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fmt</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">timetuple</span><span class="p">())</span></span><a href="#l751"></a>
<span id="l752"></span><a href="#l752"></a>
<span id="l753">    <span class="k">def</span> <span class="nf">__format__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fmt</span><span class="p">):</span></span><a href="#l753"></a>
<span id="l754">        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">fmt</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span></span><a href="#l754"></a>
<span id="l755">            <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="s">&quot;must be str, not </span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="nb">type</span><span class="p">(</span><span class="n">fmt</span><span class="p">)</span><span class="o">.</span><span class="n">__name__</span><span class="p">)</span></span><a href="#l755"></a>
<span id="l756">        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">fmt</span><span class="p">)</span> <span class="o">!=</span> <span class="mi">0</span><span class="p">:</span></span><a href="#l756"></a>
<span id="l757">            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">strftime</span><span class="p">(</span><span class="n">fmt</span><span class="p">)</span></span><a href="#l757"></a>
<span id="l758">        <span class="k">return</span> <span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span></span><a href="#l758"></a>
<span id="l759"></span><a href="#l759"></a>
<span id="l760">    <span class="k">def</span> <span class="nf">isoformat</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l760"></a>
<span id="l761">        <span class="sd">&quot;&quot;&quot;Return the date formatted according to ISO.</span></span><a href="#l761"></a>
<span id="l762"></span><a href="#l762"></a>
<span id="l763"><span class="sd">        This is &#39;YYYY-MM-DD&#39;.</span></span><a href="#l763"></a>
<span id="l764"></span><a href="#l764"></a>
<span id="l765"><span class="sd">        References:</span></span><a href="#l765"></a>
<span id="l766"><span class="sd">        - http://www.w3.org/TR/NOTE-datetime</span></span><a href="#l766"></a>
<span id="l767"><span class="sd">        - http://www.cl.cam.ac.uk/~mgk25/iso-time.html</span></span><a href="#l767"></a>
<span id="l768"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l768"></a>
<span id="l769">        <span class="k">return</span> <span class="s">&quot;</span><span class="si">%04d</span><span class="s">-</span><span class="si">%02d</span><span class="s">-</span><span class="si">%02d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_year</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_month</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_day</span><span class="p">)</span></span><a href="#l769"></a>
<span id="l770"></span><a href="#l770"></a>
<span id="l771">    <span class="n">__str__</span> <span class="o">=</span> <span class="n">isoformat</span></span><a href="#l771"></a>
<span id="l772"></span><a href="#l772"></a>
<span id="l773">    <span class="c"># Read-only field accessors</span></span><a href="#l773"></a>
<span id="l774">    <span class="nd">@property</span></span><a href="#l774"></a>
<span id="l775">    <span class="k">def</span> <span class="nf">year</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l775"></a>
<span id="l776">        <span class="sd">&quot;&quot;&quot;year (1-9999)&quot;&quot;&quot;</span></span><a href="#l776"></a>
<span id="l777">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_year</span></span><a href="#l777"></a>
<span id="l778"></span><a href="#l778"></a>
<span id="l779">    <span class="nd">@property</span></span><a href="#l779"></a>
<span id="l780">    <span class="k">def</span> <span class="nf">month</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l780"></a>
<span id="l781">        <span class="sd">&quot;&quot;&quot;month (1-12)&quot;&quot;&quot;</span></span><a href="#l781"></a>
<span id="l782">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_month</span></span><a href="#l782"></a>
<span id="l783"></span><a href="#l783"></a>
<span id="l784">    <span class="nd">@property</span></span><a href="#l784"></a>
<span id="l785">    <span class="k">def</span> <span class="nf">day</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l785"></a>
<span id="l786">        <span class="sd">&quot;&quot;&quot;day (1-31)&quot;&quot;&quot;</span></span><a href="#l786"></a>
<span id="l787">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_day</span></span><a href="#l787"></a>
<span id="l788"></span><a href="#l788"></a>
<span id="l789">    <span class="c"># Standard conversions, __eq__, __le__, __lt__, __ge__, __gt__,</span></span><a href="#l789"></a>
<span id="l790">    <span class="c"># __hash__ (and helpers)</span></span><a href="#l790"></a>
<span id="l791"></span><a href="#l791"></a>
<span id="l792">    <span class="k">def</span> <span class="nf">timetuple</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l792"></a>
<span id="l793">        <span class="s">&quot;Return local time tuple compatible with time.localtime().&quot;</span></span><a href="#l793"></a>
<span id="l794">        <span class="k">return</span> <span class="n">_build_struct_time</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_year</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_month</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_day</span><span class="p">,</span></span><a href="#l794"></a>
<span id="l795">                                  <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">)</span></span><a href="#l795"></a>
<span id="l796"></span><a href="#l796"></a>
<span id="l797">    <span class="k">def</span> <span class="nf">toordinal</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l797"></a>
<span id="l798">        <span class="sd">&quot;&quot;&quot;Return proleptic Gregorian ordinal for the year, month and day.</span></span><a href="#l798"></a>
<span id="l799"></span><a href="#l799"></a>
<span id="l800"><span class="sd">        January 1 of year 1 is day 1.  Only the year, month and day values</span></span><a href="#l800"></a>
<span id="l801"><span class="sd">        contribute to the result.</span></span><a href="#l801"></a>
<span id="l802"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l802"></a>
<span id="l803">        <span class="k">return</span> <span class="n">_ymd2ord</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_year</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_month</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_day</span><span class="p">)</span></span><a href="#l803"></a>
<span id="l804"></span><a href="#l804"></a>
<span id="l805">    <span class="k">def</span> <span class="nf">replace</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">year</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">month</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">day</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l805"></a>
<span id="l806">        <span class="sd">&quot;&quot;&quot;Return a new date with new values for the specified fields.&quot;&quot;&quot;</span></span><a href="#l806"></a>
<span id="l807">        <span class="k">if</span> <span class="n">year</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l807"></a>
<span id="l808">            <span class="n">year</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_year</span></span><a href="#l808"></a>
<span id="l809">        <span class="k">if</span> <span class="n">month</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l809"></a>
<span id="l810">            <span class="n">month</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_month</span></span><a href="#l810"></a>
<span id="l811">        <span class="k">if</span> <span class="n">day</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l811"></a>
<span id="l812">            <span class="n">day</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_day</span></span><a href="#l812"></a>
<span id="l813">        <span class="k">return</span> <span class="n">date</span><span class="p">(</span><span class="n">year</span><span class="p">,</span> <span class="n">month</span><span class="p">,</span> <span class="n">day</span><span class="p">)</span></span><a href="#l813"></a>
<span id="l814"></span><a href="#l814"></a>
<span id="l815">    <span class="c"># Comparisons of date objects with other.</span></span><a href="#l815"></a>
<span id="l816"></span><a href="#l816"></a>
<span id="l817">    <span class="k">def</span> <span class="nf">__eq__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l817"></a>
<span id="l818">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">date</span><span class="p">):</span></span><a href="#l818"></a>
<span id="l819">            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cmp</span><span class="p">(</span><span class="n">other</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span></span><a href="#l819"></a>
<span id="l820">        <span class="k">return</span> <span class="bp">NotImplemented</span></span><a href="#l820"></a>
<span id="l821"></span><a href="#l821"></a>
<span id="l822">    <span class="k">def</span> <span class="nf">__le__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l822"></a>
<span id="l823">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">date</span><span class="p">):</span></span><a href="#l823"></a>
<span id="l824">            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cmp</span><span class="p">(</span><span class="n">other</span><span class="p">)</span> <span class="o">&lt;=</span> <span class="mi">0</span></span><a href="#l824"></a>
<span id="l825">        <span class="k">return</span> <span class="bp">NotImplemented</span></span><a href="#l825"></a>
<span id="l826"></span><a href="#l826"></a>
<span id="l827">    <span class="k">def</span> <span class="nf">__lt__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l827"></a>
<span id="l828">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">date</span><span class="p">):</span></span><a href="#l828"></a>
<span id="l829">            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cmp</span><span class="p">(</span><span class="n">other</span><span class="p">)</span> <span class="o">&lt;</span> <span class="mi">0</span></span><a href="#l829"></a>
<span id="l830">        <span class="k">return</span> <span class="bp">NotImplemented</span></span><a href="#l830"></a>
<span id="l831"></span><a href="#l831"></a>
<span id="l832">    <span class="k">def</span> <span class="nf">__ge__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l832"></a>
<span id="l833">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">date</span><span class="p">):</span></span><a href="#l833"></a>
<span id="l834">            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cmp</span><span class="p">(</span><span class="n">other</span><span class="p">)</span> <span class="o">&gt;=</span> <span class="mi">0</span></span><a href="#l834"></a>
<span id="l835">        <span class="k">return</span> <span class="bp">NotImplemented</span></span><a href="#l835"></a>
<span id="l836"></span><a href="#l836"></a>
<span id="l837">    <span class="k">def</span> <span class="nf">__gt__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l837"></a>
<span id="l838">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">date</span><span class="p">):</span></span><a href="#l838"></a>
<span id="l839">            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cmp</span><span class="p">(</span><span class="n">other</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span></span><a href="#l839"></a>
<span id="l840">        <span class="k">return</span> <span class="bp">NotImplemented</span></span><a href="#l840"></a>
<span id="l841"></span><a href="#l841"></a>
<span id="l842">    <span class="k">def</span> <span class="nf">_cmp</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l842"></a>
<span id="l843">        <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">date</span><span class="p">)</span></span><a href="#l843"></a>
<span id="l844">        <span class="n">y</span><span class="p">,</span> <span class="n">m</span><span class="p">,</span> <span class="n">d</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_year</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_month</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_day</span></span><a href="#l844"></a>
<span id="l845">        <span class="n">y2</span><span class="p">,</span> <span class="n">m2</span><span class="p">,</span> <span class="n">d2</span> <span class="o">=</span> <span class="n">other</span><span class="o">.</span><span class="n">_year</span><span class="p">,</span> <span class="n">other</span><span class="o">.</span><span class="n">_month</span><span class="p">,</span> <span class="n">other</span><span class="o">.</span><span class="n">_day</span></span><a href="#l845"></a>
<span id="l846">        <span class="k">return</span> <span class="n">_cmp</span><span class="p">((</span><span class="n">y</span><span class="p">,</span> <span class="n">m</span><span class="p">,</span> <span class="n">d</span><span class="p">),</span> <span class="p">(</span><span class="n">y2</span><span class="p">,</span> <span class="n">m2</span><span class="p">,</span> <span class="n">d2</span><span class="p">))</span></span><a href="#l846"></a>
<span id="l847"></span><a href="#l847"></a>
<span id="l848">    <span class="k">def</span> <span class="nf">__hash__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l848"></a>
<span id="l849">        <span class="s">&quot;Hash.&quot;</span></span><a href="#l849"></a>
<span id="l850">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_hashcode</span> <span class="o">==</span> <span class="o">-</span><span class="mi">1</span><span class="p">:</span></span><a href="#l850"></a>
<span id="l851">            <span class="bp">self</span><span class="o">.</span><span class="n">_hashcode</span> <span class="o">=</span> <span class="nb">hash</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_getstate</span><span class="p">())</span></span><a href="#l851"></a>
<span id="l852">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_hashcode</span></span><a href="#l852"></a>
<span id="l853"></span><a href="#l853"></a>
<span id="l854">    <span class="c"># Computations</span></span><a href="#l854"></a>
<span id="l855"></span><a href="#l855"></a>
<span id="l856">    <span class="k">def</span> <span class="nf">__add__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l856"></a>
<span id="l857">        <span class="s">&quot;Add a date to a timedelta.&quot;</span></span><a href="#l857"></a>
<span id="l858">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">timedelta</span><span class="p">):</span></span><a href="#l858"></a>
<span id="l859">            <span class="n">o</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">toordinal</span><span class="p">()</span> <span class="o">+</span> <span class="n">other</span><span class="o">.</span><span class="n">days</span></span><a href="#l859"></a>
<span id="l860">            <span class="k">if</span> <span class="mi">0</span> <span class="o">&lt;</span> <span class="n">o</span> <span class="o">&lt;=</span> <span class="n">_MAXORDINAL</span><span class="p">:</span></span><a href="#l860"></a>
<span id="l861">                <span class="k">return</span> <span class="n">date</span><span class="o">.</span><span class="n">fromordinal</span><span class="p">(</span><span class="n">o</span><span class="p">)</span></span><a href="#l861"></a>
<span id="l862">            <span class="k">raise</span> <span class="ne">OverflowError</span><span class="p">(</span><span class="s">&quot;result out of range&quot;</span><span class="p">)</span></span><a href="#l862"></a>
<span id="l863">        <span class="k">return</span> <span class="bp">NotImplemented</span></span><a href="#l863"></a>
<span id="l864"></span><a href="#l864"></a>
<span id="l865">    <span class="n">__radd__</span> <span class="o">=</span> <span class="n">__add__</span></span><a href="#l865"></a>
<span id="l866"></span><a href="#l866"></a>
<span id="l867">    <span class="k">def</span> <span class="nf">__sub__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l867"></a>
<span id="l868">        <span class="sd">&quot;&quot;&quot;Subtract two dates, or a date and a timedelta.&quot;&quot;&quot;</span></span><a href="#l868"></a>
<span id="l869">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">timedelta</span><span class="p">):</span></span><a href="#l869"></a>
<span id="l870">            <span class="k">return</span> <span class="bp">self</span> <span class="o">+</span> <span class="n">timedelta</span><span class="p">(</span><span class="o">-</span><span class="n">other</span><span class="o">.</span><span class="n">days</span><span class="p">)</span></span><a href="#l870"></a>
<span id="l871">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">date</span><span class="p">):</span></span><a href="#l871"></a>
<span id="l872">            <span class="n">days1</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">toordinal</span><span class="p">()</span></span><a href="#l872"></a>
<span id="l873">            <span class="n">days2</span> <span class="o">=</span> <span class="n">other</span><span class="o">.</span><span class="n">toordinal</span><span class="p">()</span></span><a href="#l873"></a>
<span id="l874">            <span class="k">return</span> <span class="n">timedelta</span><span class="p">(</span><span class="n">days1</span> <span class="o">-</span> <span class="n">days2</span><span class="p">)</span></span><a href="#l874"></a>
<span id="l875">        <span class="k">return</span> <span class="bp">NotImplemented</span></span><a href="#l875"></a>
<span id="l876"></span><a href="#l876"></a>
<span id="l877">    <span class="k">def</span> <span class="nf">weekday</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l877"></a>
<span id="l878">        <span class="s">&quot;Return day of the week, where Monday == 0 ... Sunday == 6.&quot;</span></span><a href="#l878"></a>
<span id="l879">        <span class="k">return</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">toordinal</span><span class="p">()</span> <span class="o">+</span> <span class="mi">6</span><span class="p">)</span> <span class="o">%</span> <span class="mi">7</span></span><a href="#l879"></a>
<span id="l880"></span><a href="#l880"></a>
<span id="l881">    <span class="c"># Day-of-the-week and week-of-the-year, according to ISO</span></span><a href="#l881"></a>
<span id="l882"></span><a href="#l882"></a>
<span id="l883">    <span class="k">def</span> <span class="nf">isoweekday</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l883"></a>
<span id="l884">        <span class="s">&quot;Return day of the week, where Monday == 1 ... Sunday == 7.&quot;</span></span><a href="#l884"></a>
<span id="l885">        <span class="c"># 1-Jan-0001 is a Monday</span></span><a href="#l885"></a>
<span id="l886">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">toordinal</span><span class="p">()</span> <span class="o">%</span> <span class="mi">7</span> <span class="ow">or</span> <span class="mi">7</span></span><a href="#l886"></a>
<span id="l887"></span><a href="#l887"></a>
<span id="l888">    <span class="k">def</span> <span class="nf">isocalendar</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l888"></a>
<span id="l889">        <span class="sd">&quot;&quot;&quot;Return a 3-tuple containing ISO year, week number, and weekday.</span></span><a href="#l889"></a>
<span id="l890"></span><a href="#l890"></a>
<span id="l891"><span class="sd">        The first ISO week of the year is the (Mon-Sun) week</span></span><a href="#l891"></a>
<span id="l892"><span class="sd">        containing the year&#39;s first Thursday; everything else derives</span></span><a href="#l892"></a>
<span id="l893"><span class="sd">        from that.</span></span><a href="#l893"></a>
<span id="l894"></span><a href="#l894"></a>
<span id="l895"><span class="sd">        The first week is 1; Monday is 1 ... Sunday is 7.</span></span><a href="#l895"></a>
<span id="l896"></span><a href="#l896"></a>
<span id="l897"><span class="sd">        ISO calendar algorithm taken from</span></span><a href="#l897"></a>
<span id="l898"><span class="sd">        http://www.phys.uu.nl/~vgent/calendar/isocalendar.htm</span></span><a href="#l898"></a>
<span id="l899"><span class="sd">        (used with permission)</span></span><a href="#l899"></a>
<span id="l900"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l900"></a>
<span id="l901">        <span class="n">year</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_year</span></span><a href="#l901"></a>
<span id="l902">        <span class="n">week1monday</span> <span class="o">=</span> <span class="n">_isoweek1monday</span><span class="p">(</span><span class="n">year</span><span class="p">)</span></span><a href="#l902"></a>
<span id="l903">        <span class="n">today</span> <span class="o">=</span> <span class="n">_ymd2ord</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_year</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_month</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_day</span><span class="p">)</span></span><a href="#l903"></a>
<span id="l904">        <span class="c"># Internally, week and day have origin 0</span></span><a href="#l904"></a>
<span id="l905">        <span class="n">week</span><span class="p">,</span> <span class="n">day</span> <span class="o">=</span> <span class="nb">divmod</span><span class="p">(</span><span class="n">today</span> <span class="o">-</span> <span class="n">week1monday</span><span class="p">,</span> <span class="mi">7</span><span class="p">)</span></span><a href="#l905"></a>
<span id="l906">        <span class="k">if</span> <span class="n">week</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span></span><a href="#l906"></a>
<span id="l907">            <span class="n">year</span> <span class="o">-=</span> <span class="mi">1</span></span><a href="#l907"></a>
<span id="l908">            <span class="n">week1monday</span> <span class="o">=</span> <span class="n">_isoweek1monday</span><span class="p">(</span><span class="n">year</span><span class="p">)</span></span><a href="#l908"></a>
<span id="l909">            <span class="n">week</span><span class="p">,</span> <span class="n">day</span> <span class="o">=</span> <span class="nb">divmod</span><span class="p">(</span><span class="n">today</span> <span class="o">-</span> <span class="n">week1monday</span><span class="p">,</span> <span class="mi">7</span><span class="p">)</span></span><a href="#l909"></a>
<span id="l910">        <span class="k">elif</span> <span class="n">week</span> <span class="o">&gt;=</span> <span class="mi">52</span><span class="p">:</span></span><a href="#l910"></a>
<span id="l911">            <span class="k">if</span> <span class="n">today</span> <span class="o">&gt;=</span> <span class="n">_isoweek1monday</span><span class="p">(</span><span class="n">year</span><span class="o">+</span><span class="mi">1</span><span class="p">):</span></span><a href="#l911"></a>
<span id="l912">                <span class="n">year</span> <span class="o">+=</span> <span class="mi">1</span></span><a href="#l912"></a>
<span id="l913">                <span class="n">week</span> <span class="o">=</span> <span class="mi">0</span></span><a href="#l913"></a>
<span id="l914">        <span class="k">return</span> <span class="n">year</span><span class="p">,</span> <span class="n">week</span><span class="o">+</span><span class="mi">1</span><span class="p">,</span> <span class="n">day</span><span class="o">+</span><span class="mi">1</span></span><a href="#l914"></a>
<span id="l915"></span><a href="#l915"></a>
<span id="l916">    <span class="c"># Pickle support.</span></span><a href="#l916"></a>
<span id="l917"></span><a href="#l917"></a>
<span id="l918">    <span class="k">def</span> <span class="nf">_getstate</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l918"></a>
<span id="l919">        <span class="n">yhi</span><span class="p">,</span> <span class="n">ylo</span> <span class="o">=</span> <span class="nb">divmod</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_year</span><span class="p">,</span> <span class="mi">256</span><span class="p">)</span></span><a href="#l919"></a>
<span id="l920">        <span class="k">return</span> <span class="nb">bytes</span><span class="p">([</span><span class="n">yhi</span><span class="p">,</span> <span class="n">ylo</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_month</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_day</span><span class="p">]),</span></span><a href="#l920"></a>
<span id="l921"></span><a href="#l921"></a>
<span id="l922">    <span class="k">def</span> <span class="nf">__setstate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">string</span><span class="p">):</span></span><a href="#l922"></a>
<span id="l923">        <span class="n">yhi</span><span class="p">,</span> <span class="n">ylo</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_month</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_day</span> <span class="o">=</span> <span class="n">string</span></span><a href="#l923"></a>
<span id="l924">        <span class="bp">self</span><span class="o">.</span><span class="n">_year</span> <span class="o">=</span> <span class="n">yhi</span> <span class="o">*</span> <span class="mi">256</span> <span class="o">+</span> <span class="n">ylo</span></span><a href="#l924"></a>
<span id="l925"></span><a href="#l925"></a>
<span id="l926">    <span class="k">def</span> <span class="nf">__reduce__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l926"></a>
<span id="l927">        <span class="k">return</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__class__</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_getstate</span><span class="p">())</span></span><a href="#l927"></a>
<span id="l928"></span><a href="#l928"></a>
<span id="l929"><span class="n">_date_class</span> <span class="o">=</span> <span class="n">date</span>  <span class="c"># so functions w/ args named &quot;date&quot; can get at the class</span></span><a href="#l929"></a>
<span id="l930"></span><a href="#l930"></a>
<span id="l931"><span class="n">date</span><span class="o">.</span><span class="n">min</span> <span class="o">=</span> <span class="n">date</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span></span><a href="#l931"></a>
<span id="l932"><span class="n">date</span><span class="o">.</span><span class="n">max</span> <span class="o">=</span> <span class="n">date</span><span class="p">(</span><span class="mi">9999</span><span class="p">,</span> <span class="mi">12</span><span class="p">,</span> <span class="mi">31</span><span class="p">)</span></span><a href="#l932"></a>
<span id="l933"><span class="n">date</span><span class="o">.</span><span class="n">resolution</span> <span class="o">=</span> <span class="n">timedelta</span><span class="p">(</span><span class="n">days</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span></span><a href="#l933"></a>
<span id="l934"></span><a href="#l934"></a>
<span id="l935"><span class="k">class</span> <span class="nc">tzinfo</span><span class="p">:</span></span><a href="#l935"></a>
<span id="l936">    <span class="sd">&quot;&quot;&quot;Abstract base class for time zone info classes.</span></span><a href="#l936"></a>
<span id="l937"></span><a href="#l937"></a>
<span id="l938"><span class="sd">    Subclasses must override the name(), utcoffset() and dst() methods.</span></span><a href="#l938"></a>
<span id="l939"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l939"></a>
<span id="l940">    <span class="n">__slots__</span> <span class="o">=</span> <span class="p">()</span></span><a href="#l940"></a>
<span id="l941"></span><a href="#l941"></a>
<span id="l942">    <span class="k">def</span> <span class="nf">tzname</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">dt</span><span class="p">):</span></span><a href="#l942"></a>
<span id="l943">        <span class="s">&quot;datetime -&gt; string name of time zone.&quot;</span></span><a href="#l943"></a>
<span id="l944">        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s">&quot;tzinfo subclass must override tzname()&quot;</span><span class="p">)</span></span><a href="#l944"></a>
<span id="l945"></span><a href="#l945"></a>
<span id="l946">    <span class="k">def</span> <span class="nf">utcoffset</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">dt</span><span class="p">):</span></span><a href="#l946"></a>
<span id="l947">        <span class="s">&quot;datetime -&gt; minutes east of UTC (negative for west of UTC)&quot;</span></span><a href="#l947"></a>
<span id="l948">        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s">&quot;tzinfo subclass must override utcoffset()&quot;</span><span class="p">)</span></span><a href="#l948"></a>
<span id="l949"></span><a href="#l949"></a>
<span id="l950">    <span class="k">def</span> <span class="nf">dst</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">dt</span><span class="p">):</span></span><a href="#l950"></a>
<span id="l951">        <span class="sd">&quot;&quot;&quot;datetime -&gt; DST offset in minutes east of UTC.</span></span><a href="#l951"></a>
<span id="l952"></span><a href="#l952"></a>
<span id="l953"><span class="sd">        Return 0 if DST not in effect.  utcoffset() must include the DST</span></span><a href="#l953"></a>
<span id="l954"><span class="sd">        offset.</span></span><a href="#l954"></a>
<span id="l955"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l955"></a>
<span id="l956">        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="s">&quot;tzinfo subclass must override dst()&quot;</span><span class="p">)</span></span><a href="#l956"></a>
<span id="l957"></span><a href="#l957"></a>
<span id="l958">    <span class="k">def</span> <span class="nf">fromutc</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">dt</span><span class="p">):</span></span><a href="#l958"></a>
<span id="l959">        <span class="s">&quot;datetime in UTC -&gt; datetime in local time.&quot;</span></span><a href="#l959"></a>
<span id="l960"></span><a href="#l960"></a>
<span id="l961">        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">dt</span><span class="p">,</span> <span class="n">datetime</span><span class="p">):</span></span><a href="#l961"></a>
<span id="l962">            <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="s">&quot;fromutc() requires a datetime argument&quot;</span><span class="p">)</span></span><a href="#l962"></a>
<span id="l963">        <span class="k">if</span> <span class="n">dt</span><span class="o">.</span><span class="n">tzinfo</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">self</span><span class="p">:</span></span><a href="#l963"></a>
<span id="l964">            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&quot;dt.tzinfo is not self&quot;</span><span class="p">)</span></span><a href="#l964"></a>
<span id="l965"></span><a href="#l965"></a>
<span id="l966">        <span class="n">dtoff</span> <span class="o">=</span> <span class="n">dt</span><span class="o">.</span><span class="n">utcoffset</span><span class="p">()</span></span><a href="#l966"></a>
<span id="l967">        <span class="k">if</span> <span class="n">dtoff</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l967"></a>
<span id="l968">            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&quot;fromutc() requires a non-None utcoffset() &quot;</span></span><a href="#l968"></a>
<span id="l969">                             <span class="s">&quot;result&quot;</span><span class="p">)</span></span><a href="#l969"></a>
<span id="l970"></span><a href="#l970"></a>
<span id="l971">        <span class="c"># See the long comment block at the end of this file for an</span></span><a href="#l971"></a>
<span id="l972">        <span class="c"># explanation of this algorithm.</span></span><a href="#l972"></a>
<span id="l973">        <span class="n">dtdst</span> <span class="o">=</span> <span class="n">dt</span><span class="o">.</span><span class="n">dst</span><span class="p">()</span></span><a href="#l973"></a>
<span id="l974">        <span class="k">if</span> <span class="n">dtdst</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l974"></a>
<span id="l975">            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&quot;fromutc() requires a non-None dst() result&quot;</span><span class="p">)</span></span><a href="#l975"></a>
<span id="l976">        <span class="n">delta</span> <span class="o">=</span> <span class="n">dtoff</span> <span class="o">-</span> <span class="n">dtdst</span></span><a href="#l976"></a>
<span id="l977">        <span class="k">if</span> <span class="n">delta</span><span class="p">:</span></span><a href="#l977"></a>
<span id="l978">            <span class="n">dt</span> <span class="o">+=</span> <span class="n">delta</span></span><a href="#l978"></a>
<span id="l979">            <span class="n">dtdst</span> <span class="o">=</span> <span class="n">dt</span><span class="o">.</span><span class="n">dst</span><span class="p">()</span></span><a href="#l979"></a>
<span id="l980">            <span class="k">if</span> <span class="n">dtdst</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l980"></a>
<span id="l981">                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&quot;fromutc(): dt.dst gave inconsistent &quot;</span></span><a href="#l981"></a>
<span id="l982">                                 <span class="s">&quot;results; cannot convert&quot;</span><span class="p">)</span></span><a href="#l982"></a>
<span id="l983">        <span class="k">return</span> <span class="n">dt</span> <span class="o">+</span> <span class="n">dtdst</span></span><a href="#l983"></a>
<span id="l984"></span><a href="#l984"></a>
<span id="l985">    <span class="c"># Pickle support.</span></span><a href="#l985"></a>
<span id="l986"></span><a href="#l986"></a>
<span id="l987">    <span class="k">def</span> <span class="nf">__reduce__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l987"></a>
<span id="l988">        <span class="n">getinitargs</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="s">&quot;__getinitargs__&quot;</span><span class="p">,</span> <span class="bp">None</span><span class="p">)</span></span><a href="#l988"></a>
<span id="l989">        <span class="k">if</span> <span class="n">getinitargs</span><span class="p">:</span></span><a href="#l989"></a>
<span id="l990">            <span class="n">args</span> <span class="o">=</span> <span class="n">getinitargs</span><span class="p">()</span></span><a href="#l990"></a>
<span id="l991">        <span class="k">else</span><span class="p">:</span></span><a href="#l991"></a>
<span id="l992">            <span class="n">args</span> <span class="o">=</span> <span class="p">()</span></span><a href="#l992"></a>
<span id="l993">        <span class="n">getstate</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="s">&quot;__getstate__&quot;</span><span class="p">,</span> <span class="bp">None</span><span class="p">)</span></span><a href="#l993"></a>
<span id="l994">        <span class="k">if</span> <span class="n">getstate</span><span class="p">:</span></span><a href="#l994"></a>
<span id="l995">            <span class="n">state</span> <span class="o">=</span> <span class="n">getstate</span><span class="p">()</span></span><a href="#l995"></a>
<span id="l996">        <span class="k">else</span><span class="p">:</span></span><a href="#l996"></a>
<span id="l997">            <span class="n">state</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="s">&quot;__dict__&quot;</span><span class="p">,</span> <span class="bp">None</span><span class="p">)</span> <span class="ow">or</span> <span class="bp">None</span></span><a href="#l997"></a>
<span id="l998">        <span class="k">if</span> <span class="n">state</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l998"></a>
<span id="l999">            <span class="k">return</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__class__</span><span class="p">,</span> <span class="n">args</span><span class="p">)</span></span><a href="#l999"></a>
<span id="l1000">        <span class="k">else</span><span class="p">:</span></span><a href="#l1000"></a>
<span id="l1001">            <span class="k">return</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__class__</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">state</span><span class="p">)</span></span><a href="#l1001"></a>
<span id="l1002"></span><a href="#l1002"></a>
<span id="l1003"><span class="n">_tzinfo_class</span> <span class="o">=</span> <span class="n">tzinfo</span></span><a href="#l1003"></a>
<span id="l1004"></span><a href="#l1004"></a>
<span id="l1005"><span class="k">class</span> <span class="nc">time</span><span class="p">:</span></span><a href="#l1005"></a>
<span id="l1006">    <span class="sd">&quot;&quot;&quot;Time with time zone.</span></span><a href="#l1006"></a>
<span id="l1007"></span><a href="#l1007"></a>
<span id="l1008"><span class="sd">    Constructors:</span></span><a href="#l1008"></a>
<span id="l1009"></span><a href="#l1009"></a>
<span id="l1010"><span class="sd">    __new__()</span></span><a href="#l1010"></a>
<span id="l1011"></span><a href="#l1011"></a>
<span id="l1012"><span class="sd">    Operators:</span></span><a href="#l1012"></a>
<span id="l1013"></span><a href="#l1013"></a>
<span id="l1014"><span class="sd">    __repr__, __str__</span></span><a href="#l1014"></a>
<span id="l1015"><span class="sd">    __eq__, __le__, __lt__, __ge__, __gt__, __hash__</span></span><a href="#l1015"></a>
<span id="l1016"></span><a href="#l1016"></a>
<span id="l1017"><span class="sd">    Methods:</span></span><a href="#l1017"></a>
<span id="l1018"></span><a href="#l1018"></a>
<span id="l1019"><span class="sd">    strftime()</span></span><a href="#l1019"></a>
<span id="l1020"><span class="sd">    isoformat()</span></span><a href="#l1020"></a>
<span id="l1021"><span class="sd">    utcoffset()</span></span><a href="#l1021"></a>
<span id="l1022"><span class="sd">    tzname()</span></span><a href="#l1022"></a>
<span id="l1023"><span class="sd">    dst()</span></span><a href="#l1023"></a>
<span id="l1024"></span><a href="#l1024"></a>
<span id="l1025"><span class="sd">    Properties (readonly):</span></span><a href="#l1025"></a>
<span id="l1026"><span class="sd">    hour, minute, second, microsecond, tzinfo</span></span><a href="#l1026"></a>
<span id="l1027"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l1027"></a>
<span id="l1028">    <span class="n">__slots__</span> <span class="o">=</span> <span class="s">&#39;_hour&#39;</span><span class="p">,</span> <span class="s">&#39;_minute&#39;</span><span class="p">,</span> <span class="s">&#39;_second&#39;</span><span class="p">,</span> <span class="s">&#39;_microsecond&#39;</span><span class="p">,</span> <span class="s">&#39;_tzinfo&#39;</span><span class="p">,</span> <span class="s">&#39;_hashcode&#39;</span></span><a href="#l1028"></a>
<span id="l1029"></span><a href="#l1029"></a>
<span id="l1030">    <span class="k">def</span> <span class="nf">__new__</span><span class="p">(</span><span class="n">cls</span><span class="p">,</span> <span class="n">hour</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">minute</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">second</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">microsecond</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">tzinfo</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l1030"></a>
<span id="l1031">        <span class="sd">&quot;&quot;&quot;Constructor.</span></span><a href="#l1031"></a>
<span id="l1032"></span><a href="#l1032"></a>
<span id="l1033"><span class="sd">        Arguments:</span></span><a href="#l1033"></a>
<span id="l1034"></span><a href="#l1034"></a>
<span id="l1035"><span class="sd">        hour, minute (required)</span></span><a href="#l1035"></a>
<span id="l1036"><span class="sd">        second, microsecond (default to zero)</span></span><a href="#l1036"></a>
<span id="l1037"><span class="sd">        tzinfo (default to None)</span></span><a href="#l1037"></a>
<span id="l1038"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l1038"></a>
<span id="l1039">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">hour</span><span class="p">,</span> <span class="nb">bytes</span><span class="p">)</span> <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="n">hour</span><span class="p">)</span> <span class="o">==</span> <span class="mi">6</span> <span class="ow">and</span> <span class="n">hour</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">&lt;</span> <span class="mi">24</span><span class="p">:</span></span><a href="#l1039"></a>
<span id="l1040">            <span class="c"># Pickle support</span></span><a href="#l1040"></a>
<span id="l1041">            <span class="bp">self</span> <span class="o">=</span> <span class="nb">object</span><span class="o">.</span><span class="n">__new__</span><span class="p">(</span><span class="n">cls</span><span class="p">)</span></span><a href="#l1041"></a>
<span id="l1042">            <span class="bp">self</span><span class="o">.</span><span class="n">__setstate</span><span class="p">(</span><span class="n">hour</span><span class="p">,</span> <span class="n">minute</span> <span class="ow">or</span> <span class="bp">None</span><span class="p">)</span></span><a href="#l1042"></a>
<span id="l1043">            <span class="bp">self</span><span class="o">.</span><span class="n">_hashcode</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span></span><a href="#l1043"></a>
<span id="l1044">            <span class="k">return</span> <span class="bp">self</span></span><a href="#l1044"></a>
<span id="l1045">        <span class="n">hour</span><span class="p">,</span> <span class="n">minute</span><span class="p">,</span> <span class="n">second</span><span class="p">,</span> <span class="n">microsecond</span> <span class="o">=</span> <span class="n">_check_time_fields</span><span class="p">(</span></span><a href="#l1045"></a>
<span id="l1046">            <span class="n">hour</span><span class="p">,</span> <span class="n">minute</span><span class="p">,</span> <span class="n">second</span><span class="p">,</span> <span class="n">microsecond</span><span class="p">)</span></span><a href="#l1046"></a>
<span id="l1047">        <span class="n">_check_tzinfo_arg</span><span class="p">(</span><span class="n">tzinfo</span><span class="p">)</span></span><a href="#l1047"></a>
<span id="l1048">        <span class="bp">self</span> <span class="o">=</span> <span class="nb">object</span><span class="o">.</span><span class="n">__new__</span><span class="p">(</span><span class="n">cls</span><span class="p">)</span></span><a href="#l1048"></a>
<span id="l1049">        <span class="bp">self</span><span class="o">.</span><span class="n">_hour</span> <span class="o">=</span> <span class="n">hour</span></span><a href="#l1049"></a>
<span id="l1050">        <span class="bp">self</span><span class="o">.</span><span class="n">_minute</span> <span class="o">=</span> <span class="n">minute</span></span><a href="#l1050"></a>
<span id="l1051">        <span class="bp">self</span><span class="o">.</span><span class="n">_second</span> <span class="o">=</span> <span class="n">second</span></span><a href="#l1051"></a>
<span id="l1052">        <span class="bp">self</span><span class="o">.</span><span class="n">_microsecond</span> <span class="o">=</span> <span class="n">microsecond</span></span><a href="#l1052"></a>
<span id="l1053">        <span class="bp">self</span><span class="o">.</span><span class="n">_tzinfo</span> <span class="o">=</span> <span class="n">tzinfo</span></span><a href="#l1053"></a>
<span id="l1054">        <span class="bp">self</span><span class="o">.</span><span class="n">_hashcode</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span></span><a href="#l1054"></a>
<span id="l1055">        <span class="k">return</span> <span class="bp">self</span></span><a href="#l1055"></a>
<span id="l1056"></span><a href="#l1056"></a>
<span id="l1057">    <span class="c"># Read-only field accessors</span></span><a href="#l1057"></a>
<span id="l1058">    <span class="nd">@property</span></span><a href="#l1058"></a>
<span id="l1059">    <span class="k">def</span> <span class="nf">hour</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1059"></a>
<span id="l1060">        <span class="sd">&quot;&quot;&quot;hour (0-23)&quot;&quot;&quot;</span></span><a href="#l1060"></a>
<span id="l1061">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_hour</span></span><a href="#l1061"></a>
<span id="l1062"></span><a href="#l1062"></a>
<span id="l1063">    <span class="nd">@property</span></span><a href="#l1063"></a>
<span id="l1064">    <span class="k">def</span> <span class="nf">minute</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1064"></a>
<span id="l1065">        <span class="sd">&quot;&quot;&quot;minute (0-59)&quot;&quot;&quot;</span></span><a href="#l1065"></a>
<span id="l1066">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_minute</span></span><a href="#l1066"></a>
<span id="l1067"></span><a href="#l1067"></a>
<span id="l1068">    <span class="nd">@property</span></span><a href="#l1068"></a>
<span id="l1069">    <span class="k">def</span> <span class="nf">second</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1069"></a>
<span id="l1070">        <span class="sd">&quot;&quot;&quot;second (0-59)&quot;&quot;&quot;</span></span><a href="#l1070"></a>
<span id="l1071">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_second</span></span><a href="#l1071"></a>
<span id="l1072"></span><a href="#l1072"></a>
<span id="l1073">    <span class="nd">@property</span></span><a href="#l1073"></a>
<span id="l1074">    <span class="k">def</span> <span class="nf">microsecond</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1074"></a>
<span id="l1075">        <span class="sd">&quot;&quot;&quot;microsecond (0-999999)&quot;&quot;&quot;</span></span><a href="#l1075"></a>
<span id="l1076">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_microsecond</span></span><a href="#l1076"></a>
<span id="l1077"></span><a href="#l1077"></a>
<span id="l1078">    <span class="nd">@property</span></span><a href="#l1078"></a>
<span id="l1079">    <span class="k">def</span> <span class="nf">tzinfo</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1079"></a>
<span id="l1080">        <span class="sd">&quot;&quot;&quot;timezone info object&quot;&quot;&quot;</span></span><a href="#l1080"></a>
<span id="l1081">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tzinfo</span></span><a href="#l1081"></a>
<span id="l1082"></span><a href="#l1082"></a>
<span id="l1083">    <span class="c"># Standard conversions, __hash__ (and helpers)</span></span><a href="#l1083"></a>
<span id="l1084"></span><a href="#l1084"></a>
<span id="l1085">    <span class="c"># Comparisons of time objects with other.</span></span><a href="#l1085"></a>
<span id="l1086"></span><a href="#l1086"></a>
<span id="l1087">    <span class="k">def</span> <span class="nf">__eq__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l1087"></a>
<span id="l1088">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">time</span><span class="p">):</span></span><a href="#l1088"></a>
<span id="l1089">            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cmp</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">allow_mixed</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span></span><a href="#l1089"></a>
<span id="l1090">        <span class="k">else</span><span class="p">:</span></span><a href="#l1090"></a>
<span id="l1091">            <span class="k">return</span> <span class="bp">False</span></span><a href="#l1091"></a>
<span id="l1092"></span><a href="#l1092"></a>
<span id="l1093">    <span class="k">def</span> <span class="nf">__le__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l1093"></a>
<span id="l1094">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">time</span><span class="p">):</span></span><a href="#l1094"></a>
<span id="l1095">            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cmp</span><span class="p">(</span><span class="n">other</span><span class="p">)</span> <span class="o">&lt;=</span> <span class="mi">0</span></span><a href="#l1095"></a>
<span id="l1096">        <span class="k">else</span><span class="p">:</span></span><a href="#l1096"></a>
<span id="l1097">            <span class="n">_cmperror</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">)</span></span><a href="#l1097"></a>
<span id="l1098"></span><a href="#l1098"></a>
<span id="l1099">    <span class="k">def</span> <span class="nf">__lt__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l1099"></a>
<span id="l1100">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">time</span><span class="p">):</span></span><a href="#l1100"></a>
<span id="l1101">            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cmp</span><span class="p">(</span><span class="n">other</span><span class="p">)</span> <span class="o">&lt;</span> <span class="mi">0</span></span><a href="#l1101"></a>
<span id="l1102">        <span class="k">else</span><span class="p">:</span></span><a href="#l1102"></a>
<span id="l1103">            <span class="n">_cmperror</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">)</span></span><a href="#l1103"></a>
<span id="l1104"></span><a href="#l1104"></a>
<span id="l1105">    <span class="k">def</span> <span class="nf">__ge__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l1105"></a>
<span id="l1106">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">time</span><span class="p">):</span></span><a href="#l1106"></a>
<span id="l1107">            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cmp</span><span class="p">(</span><span class="n">other</span><span class="p">)</span> <span class="o">&gt;=</span> <span class="mi">0</span></span><a href="#l1107"></a>
<span id="l1108">        <span class="k">else</span><span class="p">:</span></span><a href="#l1108"></a>
<span id="l1109">            <span class="n">_cmperror</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">)</span></span><a href="#l1109"></a>
<span id="l1110"></span><a href="#l1110"></a>
<span id="l1111">    <span class="k">def</span> <span class="nf">__gt__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l1111"></a>
<span id="l1112">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">time</span><span class="p">):</span></span><a href="#l1112"></a>
<span id="l1113">            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cmp</span><span class="p">(</span><span class="n">other</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span></span><a href="#l1113"></a>
<span id="l1114">        <span class="k">else</span><span class="p">:</span></span><a href="#l1114"></a>
<span id="l1115">            <span class="n">_cmperror</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">)</span></span><a href="#l1115"></a>
<span id="l1116"></span><a href="#l1116"></a>
<span id="l1117">    <span class="k">def</span> <span class="nf">_cmp</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">,</span> <span class="n">allow_mixed</span><span class="o">=</span><span class="bp">False</span><span class="p">):</span></span><a href="#l1117"></a>
<span id="l1118">        <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">time</span><span class="p">)</span></span><a href="#l1118"></a>
<span id="l1119">        <span class="n">mytz</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tzinfo</span></span><a href="#l1119"></a>
<span id="l1120">        <span class="n">ottz</span> <span class="o">=</span> <span class="n">other</span><span class="o">.</span><span class="n">_tzinfo</span></span><a href="#l1120"></a>
<span id="l1121">        <span class="n">myoff</span> <span class="o">=</span> <span class="n">otoff</span> <span class="o">=</span> <span class="bp">None</span></span><a href="#l1121"></a>
<span id="l1122"></span><a href="#l1122"></a>
<span id="l1123">        <span class="k">if</span> <span class="n">mytz</span> <span class="ow">is</span> <span class="n">ottz</span><span class="p">:</span></span><a href="#l1123"></a>
<span id="l1124">            <span class="n">base_compare</span> <span class="o">=</span> <span class="bp">True</span></span><a href="#l1124"></a>
<span id="l1125">        <span class="k">else</span><span class="p">:</span></span><a href="#l1125"></a>
<span id="l1126">            <span class="n">myoff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">utcoffset</span><span class="p">()</span></span><a href="#l1126"></a>
<span id="l1127">            <span class="n">otoff</span> <span class="o">=</span> <span class="n">other</span><span class="o">.</span><span class="n">utcoffset</span><span class="p">()</span></span><a href="#l1127"></a>
<span id="l1128">            <span class="n">base_compare</span> <span class="o">=</span> <span class="n">myoff</span> <span class="o">==</span> <span class="n">otoff</span></span><a href="#l1128"></a>
<span id="l1129"></span><a href="#l1129"></a>
<span id="l1130">        <span class="k">if</span> <span class="n">base_compare</span><span class="p">:</span></span><a href="#l1130"></a>
<span id="l1131">            <span class="k">return</span> <span class="n">_cmp</span><span class="p">((</span><span class="bp">self</span><span class="o">.</span><span class="n">_hour</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_minute</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_second</span><span class="p">,</span></span><a href="#l1131"></a>
<span id="l1132">                         <span class="bp">self</span><span class="o">.</span><span class="n">_microsecond</span><span class="p">),</span></span><a href="#l1132"></a>
<span id="l1133">                        <span class="p">(</span><span class="n">other</span><span class="o">.</span><span class="n">_hour</span><span class="p">,</span> <span class="n">other</span><span class="o">.</span><span class="n">_minute</span><span class="p">,</span> <span class="n">other</span><span class="o">.</span><span class="n">_second</span><span class="p">,</span></span><a href="#l1133"></a>
<span id="l1134">                         <span class="n">other</span><span class="o">.</span><span class="n">_microsecond</span><span class="p">))</span></span><a href="#l1134"></a>
<span id="l1135">        <span class="k">if</span> <span class="n">myoff</span> <span class="ow">is</span> <span class="bp">None</span> <span class="ow">or</span> <span class="n">otoff</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1135"></a>
<span id="l1136">            <span class="k">if</span> <span class="n">allow_mixed</span><span class="p">:</span></span><a href="#l1136"></a>
<span id="l1137">                <span class="k">return</span> <span class="mi">2</span> <span class="c"># arbitrary non-zero value</span></span><a href="#l1137"></a>
<span id="l1138">            <span class="k">else</span><span class="p">:</span></span><a href="#l1138"></a>
<span id="l1139">                <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="s">&quot;cannot compare naive and aware times&quot;</span><span class="p">)</span></span><a href="#l1139"></a>
<span id="l1140">        <span class="n">myhhmm</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_hour</span> <span class="o">*</span> <span class="mi">60</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">_minute</span> <span class="o">-</span> <span class="n">myoff</span><span class="o">//</span><span class="n">timedelta</span><span class="p">(</span><span class="n">minutes</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span></span><a href="#l1140"></a>
<span id="l1141">        <span class="n">othhmm</span> <span class="o">=</span> <span class="n">other</span><span class="o">.</span><span class="n">_hour</span> <span class="o">*</span> <span class="mi">60</span> <span class="o">+</span> <span class="n">other</span><span class="o">.</span><span class="n">_minute</span> <span class="o">-</span> <span class="n">otoff</span><span class="o">//</span><span class="n">timedelta</span><span class="p">(</span><span class="n">minutes</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span></span><a href="#l1141"></a>
<span id="l1142">        <span class="k">return</span> <span class="n">_cmp</span><span class="p">((</span><span class="n">myhhmm</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_second</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_microsecond</span><span class="p">),</span></span><a href="#l1142"></a>
<span id="l1143">                    <span class="p">(</span><span class="n">othhmm</span><span class="p">,</span> <span class="n">other</span><span class="o">.</span><span class="n">_second</span><span class="p">,</span> <span class="n">other</span><span class="o">.</span><span class="n">_microsecond</span><span class="p">))</span></span><a href="#l1143"></a>
<span id="l1144"></span><a href="#l1144"></a>
<span id="l1145">    <span class="k">def</span> <span class="nf">__hash__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1145"></a>
<span id="l1146">        <span class="sd">&quot;&quot;&quot;Hash.&quot;&quot;&quot;</span></span><a href="#l1146"></a>
<span id="l1147">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_hashcode</span> <span class="o">==</span> <span class="o">-</span><span class="mi">1</span><span class="p">:</span></span><a href="#l1147"></a>
<span id="l1148">            <span class="n">tzoff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">utcoffset</span><span class="p">()</span></span><a href="#l1148"></a>
<span id="l1149">            <span class="k">if</span> <span class="ow">not</span> <span class="n">tzoff</span><span class="p">:</span>  <span class="c"># zero or None</span></span><a href="#l1149"></a>
<span id="l1150">                <span class="bp">self</span><span class="o">.</span><span class="n">_hashcode</span> <span class="o">=</span> <span class="nb">hash</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_getstate</span><span class="p">()[</span><span class="mi">0</span><span class="p">])</span></span><a href="#l1150"></a>
<span id="l1151">            <span class="k">else</span><span class="p">:</span></span><a href="#l1151"></a>
<span id="l1152">                <span class="n">h</span><span class="p">,</span> <span class="n">m</span> <span class="o">=</span> <span class="nb">divmod</span><span class="p">(</span><span class="n">timedelta</span><span class="p">(</span><span class="n">hours</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">hour</span><span class="p">,</span> <span class="n">minutes</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">minute</span><span class="p">)</span> <span class="o">-</span> <span class="n">tzoff</span><span class="p">,</span></span><a href="#l1152"></a>
<span id="l1153">                              <span class="n">timedelta</span><span class="p">(</span><span class="n">hours</span><span class="o">=</span><span class="mi">1</span><span class="p">))</span></span><a href="#l1153"></a>
<span id="l1154">                <span class="k">assert</span> <span class="ow">not</span> <span class="n">m</span> <span class="o">%</span> <span class="n">timedelta</span><span class="p">(</span><span class="n">minutes</span><span class="o">=</span><span class="mi">1</span><span class="p">),</span> <span class="s">&quot;whole minute&quot;</span></span><a href="#l1154"></a>
<span id="l1155">                <span class="n">m</span> <span class="o">//=</span> <span class="n">timedelta</span><span class="p">(</span><span class="n">minutes</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span></span><a href="#l1155"></a>
<span id="l1156">                <span class="k">if</span> <span class="mi">0</span> <span class="o">&lt;=</span> <span class="n">h</span> <span class="o">&lt;</span> <span class="mi">24</span><span class="p">:</span></span><a href="#l1156"></a>
<span id="l1157">                    <span class="bp">self</span><span class="o">.</span><span class="n">_hashcode</span> <span class="o">=</span> <span class="nb">hash</span><span class="p">(</span><span class="n">time</span><span class="p">(</span><span class="n">h</span><span class="p">,</span> <span class="n">m</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">second</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">microsecond</span><span class="p">))</span></span><a href="#l1157"></a>
<span id="l1158">                <span class="k">else</span><span class="p">:</span></span><a href="#l1158"></a>
<span id="l1159">                    <span class="bp">self</span><span class="o">.</span><span class="n">_hashcode</span> <span class="o">=</span> <span class="nb">hash</span><span class="p">((</span><span class="n">h</span><span class="p">,</span> <span class="n">m</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">second</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">microsecond</span><span class="p">))</span></span><a href="#l1159"></a>
<span id="l1160">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_hashcode</span></span><a href="#l1160"></a>
<span id="l1161"></span><a href="#l1161"></a>
<span id="l1162">    <span class="c"># Conversion to string</span></span><a href="#l1162"></a>
<span id="l1163"></span><a href="#l1163"></a>
<span id="l1164">    <span class="k">def</span> <span class="nf">_tzstr</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">sep</span><span class="o">=</span><span class="s">&quot;:&quot;</span><span class="p">):</span></span><a href="#l1164"></a>
<span id="l1165">        <span class="sd">&quot;&quot;&quot;Return formatted timezone offset (+xx:xx) or None.&quot;&quot;&quot;</span></span><a href="#l1165"></a>
<span id="l1166">        <span class="n">off</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">utcoffset</span><span class="p">()</span></span><a href="#l1166"></a>
<span id="l1167">        <span class="k">if</span> <span class="n">off</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1167"></a>
<span id="l1168">            <span class="k">if</span> <span class="n">off</span><span class="o">.</span><span class="n">days</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span></span><a href="#l1168"></a>
<span id="l1169">                <span class="n">sign</span> <span class="o">=</span> <span class="s">&quot;-&quot;</span></span><a href="#l1169"></a>
<span id="l1170">                <span class="n">off</span> <span class="o">=</span> <span class="o">-</span><span class="n">off</span></span><a href="#l1170"></a>
<span id="l1171">            <span class="k">else</span><span class="p">:</span></span><a href="#l1171"></a>
<span id="l1172">                <span class="n">sign</span> <span class="o">=</span> <span class="s">&quot;+&quot;</span></span><a href="#l1172"></a>
<span id="l1173">            <span class="n">hh</span><span class="p">,</span> <span class="n">mm</span> <span class="o">=</span> <span class="nb">divmod</span><span class="p">(</span><span class="n">off</span><span class="p">,</span> <span class="n">timedelta</span><span class="p">(</span><span class="n">hours</span><span class="o">=</span><span class="mi">1</span><span class="p">))</span></span><a href="#l1173"></a>
<span id="l1174">            <span class="k">assert</span> <span class="ow">not</span> <span class="n">mm</span> <span class="o">%</span> <span class="n">timedelta</span><span class="p">(</span><span class="n">minutes</span><span class="o">=</span><span class="mi">1</span><span class="p">),</span> <span class="s">&quot;whole minute&quot;</span></span><a href="#l1174"></a>
<span id="l1175">            <span class="n">mm</span> <span class="o">//=</span> <span class="n">timedelta</span><span class="p">(</span><span class="n">minutes</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span></span><a href="#l1175"></a>
<span id="l1176">            <span class="k">assert</span> <span class="mi">0</span> <span class="o">&lt;=</span> <span class="n">hh</span> <span class="o">&lt;</span> <span class="mi">24</span></span><a href="#l1176"></a>
<span id="l1177">            <span class="n">off</span> <span class="o">=</span> <span class="s">&quot;</span><span class="si">%s%02d%s%02d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">sign</span><span class="p">,</span> <span class="n">hh</span><span class="p">,</span> <span class="n">sep</span><span class="p">,</span> <span class="n">mm</span><span class="p">)</span></span><a href="#l1177"></a>
<span id="l1178">        <span class="k">return</span> <span class="n">off</span></span><a href="#l1178"></a>
<span id="l1179"></span><a href="#l1179"></a>
<span id="l1180">    <span class="k">def</span> <span class="nf">__repr__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1180"></a>
<span id="l1181">        <span class="sd">&quot;&quot;&quot;Convert to formal string, for repr().&quot;&quot;&quot;</span></span><a href="#l1181"></a>
<span id="l1182">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_microsecond</span> <span class="o">!=</span> <span class="mi">0</span><span class="p">:</span></span><a href="#l1182"></a>
<span id="l1183">            <span class="n">s</span> <span class="o">=</span> <span class="s">&quot;, </span><span class="si">%d</span><span class="s">, </span><span class="si">%d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_second</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_microsecond</span><span class="p">)</span></span><a href="#l1183"></a>
<span id="l1184">        <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">_second</span> <span class="o">!=</span> <span class="mi">0</span><span class="p">:</span></span><a href="#l1184"></a>
<span id="l1185">            <span class="n">s</span> <span class="o">=</span> <span class="s">&quot;, </span><span class="si">%d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="bp">self</span><span class="o">.</span><span class="n">_second</span></span><a href="#l1185"></a>
<span id="l1186">        <span class="k">else</span><span class="p">:</span></span><a href="#l1186"></a>
<span id="l1187">            <span class="n">s</span> <span class="o">=</span> <span class="s">&quot;&quot;</span></span><a href="#l1187"></a>
<span id="l1188">        <span class="n">s</span><span class="o">=</span> <span class="s">&quot;</span><span class="si">%s</span><span class="s">.</span><span class="si">%s</span><span class="s">(</span><span class="si">%d</span><span class="s">, </span><span class="si">%d%s</span><span class="s">)&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__class__</span><span class="o">.</span><span class="n">__module__</span><span class="p">,</span></span><a href="#l1188"></a>
<span id="l1189">                                <span class="bp">self</span><span class="o">.</span><span class="n">__class__</span><span class="o">.</span><span class="n">__qualname__</span><span class="p">,</span></span><a href="#l1189"></a>
<span id="l1190">                                <span class="bp">self</span><span class="o">.</span><span class="n">_hour</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_minute</span><span class="p">,</span> <span class="n">s</span><span class="p">)</span></span><a href="#l1190"></a>
<span id="l1191">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tzinfo</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1191"></a>
<span id="l1192">            <span class="k">assert</span> <span class="n">s</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">:]</span> <span class="o">==</span> <span class="s">&quot;)&quot;</span></span><a href="#l1192"></a>
<span id="l1193">            <span class="n">s</span> <span class="o">=</span> <span class="n">s</span><span class="p">[:</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span> <span class="o">+</span> <span class="s">&quot;, tzinfo=</span><span class="si">%r</span><span class="s">&quot;</span> <span class="o">%</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tzinfo</span> <span class="o">+</span> <span class="s">&quot;)&quot;</span></span><a href="#l1193"></a>
<span id="l1194">        <span class="k">return</span> <span class="n">s</span></span><a href="#l1194"></a>
<span id="l1195"></span><a href="#l1195"></a>
<span id="l1196">    <span class="k">def</span> <span class="nf">isoformat</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1196"></a>
<span id="l1197">        <span class="sd">&quot;&quot;&quot;Return the time formatted according to ISO.</span></span><a href="#l1197"></a>
<span id="l1198"></span><a href="#l1198"></a>
<span id="l1199"><span class="sd">        This is &#39;HH:MM:SS.mmmmmm+zz:zz&#39;, or &#39;HH:MM:SS+zz:zz&#39; if</span></span><a href="#l1199"></a>
<span id="l1200"><span class="sd">        self.microsecond == 0.</span></span><a href="#l1200"></a>
<span id="l1201"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l1201"></a>
<span id="l1202">        <span class="n">s</span> <span class="o">=</span> <span class="n">_format_time</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_hour</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_minute</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_second</span><span class="p">,</span></span><a href="#l1202"></a>
<span id="l1203">                         <span class="bp">self</span><span class="o">.</span><span class="n">_microsecond</span><span class="p">)</span></span><a href="#l1203"></a>
<span id="l1204">        <span class="n">tz</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tzstr</span><span class="p">()</span></span><a href="#l1204"></a>
<span id="l1205">        <span class="k">if</span> <span class="n">tz</span><span class="p">:</span></span><a href="#l1205"></a>
<span id="l1206">            <span class="n">s</span> <span class="o">+=</span> <span class="n">tz</span></span><a href="#l1206"></a>
<span id="l1207">        <span class="k">return</span> <span class="n">s</span></span><a href="#l1207"></a>
<span id="l1208"></span><a href="#l1208"></a>
<span id="l1209">    <span class="n">__str__</span> <span class="o">=</span> <span class="n">isoformat</span></span><a href="#l1209"></a>
<span id="l1210"></span><a href="#l1210"></a>
<span id="l1211">    <span class="k">def</span> <span class="nf">strftime</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fmt</span><span class="p">):</span></span><a href="#l1211"></a>
<span id="l1212">        <span class="sd">&quot;&quot;&quot;Format using strftime().  The date part of the timestamp passed</span></span><a href="#l1212"></a>
<span id="l1213"><span class="sd">        to underlying strftime should not be used.</span></span><a href="#l1213"></a>
<span id="l1214"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l1214"></a>
<span id="l1215">        <span class="c"># The year must be &gt;= 1000 else Python&#39;s strftime implementation</span></span><a href="#l1215"></a>
<span id="l1216">        <span class="c"># can raise a bogus exception.</span></span><a href="#l1216"></a>
<span id="l1217">        <span class="n">timetuple</span> <span class="o">=</span> <span class="p">(</span><span class="mi">1900</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span></span><a href="#l1217"></a>
<span id="l1218">                     <span class="bp">self</span><span class="o">.</span><span class="n">_hour</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_minute</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_second</span><span class="p">,</span></span><a href="#l1218"></a>
<span id="l1219">                     <span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">)</span></span><a href="#l1219"></a>
<span id="l1220">        <span class="k">return</span> <span class="n">_wrap_strftime</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fmt</span><span class="p">,</span> <span class="n">timetuple</span><span class="p">)</span></span><a href="#l1220"></a>
<span id="l1221"></span><a href="#l1221"></a>
<span id="l1222">    <span class="k">def</span> <span class="nf">__format__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fmt</span><span class="p">):</span></span><a href="#l1222"></a>
<span id="l1223">        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">fmt</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span></span><a href="#l1223"></a>
<span id="l1224">            <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="s">&quot;must be str, not </span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="nb">type</span><span class="p">(</span><span class="n">fmt</span><span class="p">)</span><span class="o">.</span><span class="n">__name__</span><span class="p">)</span></span><a href="#l1224"></a>
<span id="l1225">        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">fmt</span><span class="p">)</span> <span class="o">!=</span> <span class="mi">0</span><span class="p">:</span></span><a href="#l1225"></a>
<span id="l1226">            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">strftime</span><span class="p">(</span><span class="n">fmt</span><span class="p">)</span></span><a href="#l1226"></a>
<span id="l1227">        <span class="k">return</span> <span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span></span><a href="#l1227"></a>
<span id="l1228"></span><a href="#l1228"></a>
<span id="l1229">    <span class="c"># Timezone functions</span></span><a href="#l1229"></a>
<span id="l1230"></span><a href="#l1230"></a>
<span id="l1231">    <span class="k">def</span> <span class="nf">utcoffset</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1231"></a>
<span id="l1232">        <span class="sd">&quot;&quot;&quot;Return the timezone offset in minutes east of UTC (negative west of</span></span><a href="#l1232"></a>
<span id="l1233"><span class="sd">        UTC).&quot;&quot;&quot;</span></span><a href="#l1233"></a>
<span id="l1234">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tzinfo</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1234"></a>
<span id="l1235">            <span class="k">return</span> <span class="bp">None</span></span><a href="#l1235"></a>
<span id="l1236">        <span class="n">offset</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tzinfo</span><span class="o">.</span><span class="n">utcoffset</span><span class="p">(</span><span class="bp">None</span><span class="p">)</span></span><a href="#l1236"></a>
<span id="l1237">        <span class="n">_check_utc_offset</span><span class="p">(</span><span class="s">&quot;utcoffset&quot;</span><span class="p">,</span> <span class="n">offset</span><span class="p">)</span></span><a href="#l1237"></a>
<span id="l1238">        <span class="k">return</span> <span class="n">offset</span></span><a href="#l1238"></a>
<span id="l1239"></span><a href="#l1239"></a>
<span id="l1240">    <span class="k">def</span> <span class="nf">tzname</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1240"></a>
<span id="l1241">        <span class="sd">&quot;&quot;&quot;Return the timezone name.</span></span><a href="#l1241"></a>
<span id="l1242"></span><a href="#l1242"></a>
<span id="l1243"><span class="sd">        Note that the name is 100% informational -- there&#39;s no requirement that</span></span><a href="#l1243"></a>
<span id="l1244"><span class="sd">        it mean anything in particular. For example, &quot;GMT&quot;, &quot;UTC&quot;, &quot;-500&quot;,</span></span><a href="#l1244"></a>
<span id="l1245"><span class="sd">        &quot;-5:00&quot;, &quot;EDT&quot;, &quot;US/Eastern&quot;, &quot;America/New York&quot; are all valid replies.</span></span><a href="#l1245"></a>
<span id="l1246"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l1246"></a>
<span id="l1247">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tzinfo</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1247"></a>
<span id="l1248">            <span class="k">return</span> <span class="bp">None</span></span><a href="#l1248"></a>
<span id="l1249">        <span class="n">name</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tzinfo</span><span class="o">.</span><span class="n">tzname</span><span class="p">(</span><span class="bp">None</span><span class="p">)</span></span><a href="#l1249"></a>
<span id="l1250">        <span class="n">_check_tzname</span><span class="p">(</span><span class="n">name</span><span class="p">)</span></span><a href="#l1250"></a>
<span id="l1251">        <span class="k">return</span> <span class="n">name</span></span><a href="#l1251"></a>
<span id="l1252"></span><a href="#l1252"></a>
<span id="l1253">    <span class="k">def</span> <span class="nf">dst</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1253"></a>
<span id="l1254">        <span class="sd">&quot;&quot;&quot;Return 0 if DST is not in effect, or the DST offset (in minutes</span></span><a href="#l1254"></a>
<span id="l1255"><span class="sd">        eastward) if DST is in effect.</span></span><a href="#l1255"></a>
<span id="l1256"></span><a href="#l1256"></a>
<span id="l1257"><span class="sd">        This is purely informational; the DST offset has already been added to</span></span><a href="#l1257"></a>
<span id="l1258"><span class="sd">        the UTC offset returned by utcoffset() if applicable, so there&#39;s no</span></span><a href="#l1258"></a>
<span id="l1259"><span class="sd">        need to consult dst() unless you&#39;re interested in displaying the DST</span></span><a href="#l1259"></a>
<span id="l1260"><span class="sd">        info.</span></span><a href="#l1260"></a>
<span id="l1261"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l1261"></a>
<span id="l1262">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tzinfo</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1262"></a>
<span id="l1263">            <span class="k">return</span> <span class="bp">None</span></span><a href="#l1263"></a>
<span id="l1264">        <span class="n">offset</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tzinfo</span><span class="o">.</span><span class="n">dst</span><span class="p">(</span><span class="bp">None</span><span class="p">)</span></span><a href="#l1264"></a>
<span id="l1265">        <span class="n">_check_utc_offset</span><span class="p">(</span><span class="s">&quot;dst&quot;</span><span class="p">,</span> <span class="n">offset</span><span class="p">)</span></span><a href="#l1265"></a>
<span id="l1266">        <span class="k">return</span> <span class="n">offset</span></span><a href="#l1266"></a>
<span id="l1267"></span><a href="#l1267"></a>
<span id="l1268">    <span class="k">def</span> <span class="nf">replace</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">hour</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">minute</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">second</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">microsecond</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></span><a href="#l1268"></a>
<span id="l1269">                <span class="n">tzinfo</span><span class="o">=</span><span class="bp">True</span><span class="p">):</span></span><a href="#l1269"></a>
<span id="l1270">        <span class="sd">&quot;&quot;&quot;Return a new time with new values for the specified fields.&quot;&quot;&quot;</span></span><a href="#l1270"></a>
<span id="l1271">        <span class="k">if</span> <span class="n">hour</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1271"></a>
<span id="l1272">            <span class="n">hour</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">hour</span></span><a href="#l1272"></a>
<span id="l1273">        <span class="k">if</span> <span class="n">minute</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1273"></a>
<span id="l1274">            <span class="n">minute</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">minute</span></span><a href="#l1274"></a>
<span id="l1275">        <span class="k">if</span> <span class="n">second</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1275"></a>
<span id="l1276">            <span class="n">second</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">second</span></span><a href="#l1276"></a>
<span id="l1277">        <span class="k">if</span> <span class="n">microsecond</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1277"></a>
<span id="l1278">            <span class="n">microsecond</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">microsecond</span></span><a href="#l1278"></a>
<span id="l1279">        <span class="k">if</span> <span class="n">tzinfo</span> <span class="ow">is</span> <span class="bp">True</span><span class="p">:</span></span><a href="#l1279"></a>
<span id="l1280">            <span class="n">tzinfo</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tzinfo</span></span><a href="#l1280"></a>
<span id="l1281">        <span class="k">return</span> <span class="n">time</span><span class="p">(</span><span class="n">hour</span><span class="p">,</span> <span class="n">minute</span><span class="p">,</span> <span class="n">second</span><span class="p">,</span> <span class="n">microsecond</span><span class="p">,</span> <span class="n">tzinfo</span><span class="p">)</span></span><a href="#l1281"></a>
<span id="l1282"></span><a href="#l1282"></a>
<span id="l1283">    <span class="c"># Pickle support.</span></span><a href="#l1283"></a>
<span id="l1284"></span><a href="#l1284"></a>
<span id="l1285">    <span class="k">def</span> <span class="nf">_getstate</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1285"></a>
<span id="l1286">        <span class="n">us2</span><span class="p">,</span> <span class="n">us3</span> <span class="o">=</span> <span class="nb">divmod</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_microsecond</span><span class="p">,</span> <span class="mi">256</span><span class="p">)</span></span><a href="#l1286"></a>
<span id="l1287">        <span class="n">us1</span><span class="p">,</span> <span class="n">us2</span> <span class="o">=</span> <span class="nb">divmod</span><span class="p">(</span><span class="n">us2</span><span class="p">,</span> <span class="mi">256</span><span class="p">)</span></span><a href="#l1287"></a>
<span id="l1288">        <span class="n">basestate</span> <span class="o">=</span> <span class="nb">bytes</span><span class="p">([</span><span class="bp">self</span><span class="o">.</span><span class="n">_hour</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_minute</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_second</span><span class="p">,</span></span><a href="#l1288"></a>
<span id="l1289">                           <span class="n">us1</span><span class="p">,</span> <span class="n">us2</span><span class="p">,</span> <span class="n">us3</span><span class="p">])</span></span><a href="#l1289"></a>
<span id="l1290">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tzinfo</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1290"></a>
<span id="l1291">            <span class="k">return</span> <span class="p">(</span><span class="n">basestate</span><span class="p">,)</span></span><a href="#l1291"></a>
<span id="l1292">        <span class="k">else</span><span class="p">:</span></span><a href="#l1292"></a>
<span id="l1293">            <span class="k">return</span> <span class="p">(</span><span class="n">basestate</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tzinfo</span><span class="p">)</span></span><a href="#l1293"></a>
<span id="l1294"></span><a href="#l1294"></a>
<span id="l1295">    <span class="k">def</span> <span class="nf">__setstate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">string</span><span class="p">,</span> <span class="n">tzinfo</span><span class="p">):</span></span><a href="#l1295"></a>
<span id="l1296">        <span class="k">if</span> <span class="n">tzinfo</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span> <span class="ow">and</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">tzinfo</span><span class="p">,</span> <span class="n">_tzinfo_class</span><span class="p">):</span></span><a href="#l1296"></a>
<span id="l1297">            <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="s">&quot;bad tzinfo state arg&quot;</span><span class="p">)</span></span><a href="#l1297"></a>
<span id="l1298">        <span class="bp">self</span><span class="o">.</span><span class="n">_hour</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_minute</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_second</span><span class="p">,</span> <span class="n">us1</span><span class="p">,</span> <span class="n">us2</span><span class="p">,</span> <span class="n">us3</span> <span class="o">=</span> <span class="n">string</span></span><a href="#l1298"></a>
<span id="l1299">        <span class="bp">self</span><span class="o">.</span><span class="n">_microsecond</span> <span class="o">=</span> <span class="p">(((</span><span class="n">us1</span> <span class="o">&lt;&lt;</span> <span class="mi">8</span><span class="p">)</span> <span class="o">|</span> <span class="n">us2</span><span class="p">)</span> <span class="o">&lt;&lt;</span> <span class="mi">8</span><span class="p">)</span> <span class="o">|</span> <span class="n">us3</span></span><a href="#l1299"></a>
<span id="l1300">        <span class="bp">self</span><span class="o">.</span><span class="n">_tzinfo</span> <span class="o">=</span> <span class="n">tzinfo</span></span><a href="#l1300"></a>
<span id="l1301"></span><a href="#l1301"></a>
<span id="l1302">    <span class="k">def</span> <span class="nf">__reduce__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1302"></a>
<span id="l1303">        <span class="k">return</span> <span class="p">(</span><span class="n">time</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_getstate</span><span class="p">())</span></span><a href="#l1303"></a>
<span id="l1304"></span><a href="#l1304"></a>
<span id="l1305"><span class="n">_time_class</span> <span class="o">=</span> <span class="n">time</span>  <span class="c"># so functions w/ args named &quot;time&quot; can get at the class</span></span><a href="#l1305"></a>
<span id="l1306"></span><a href="#l1306"></a>
<span id="l1307"><span class="n">time</span><span class="o">.</span><span class="n">min</span> <span class="o">=</span> <span class="n">time</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span></span><a href="#l1307"></a>
<span id="l1308"><span class="n">time</span><span class="o">.</span><span class="n">max</span> <span class="o">=</span> <span class="n">time</span><span class="p">(</span><span class="mi">23</span><span class="p">,</span> <span class="mi">59</span><span class="p">,</span> <span class="mi">59</span><span class="p">,</span> <span class="mi">999999</span><span class="p">)</span></span><a href="#l1308"></a>
<span id="l1309"><span class="n">time</span><span class="o">.</span><span class="n">resolution</span> <span class="o">=</span> <span class="n">timedelta</span><span class="p">(</span><span class="n">microseconds</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span></span><a href="#l1309"></a>
<span id="l1310"></span><a href="#l1310"></a>
<span id="l1311"><span class="k">class</span> <span class="nc">datetime</span><span class="p">(</span><span class="n">date</span><span class="p">):</span></span><a href="#l1311"></a>
<span id="l1312">    <span class="sd">&quot;&quot;&quot;datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])</span></span><a href="#l1312"></a>
<span id="l1313"></span><a href="#l1313"></a>
<span id="l1314"><span class="sd">    The year, month and day arguments are required. tzinfo may be None, or an</span></span><a href="#l1314"></a>
<span id="l1315"><span class="sd">    instance of a tzinfo subclass. The remaining arguments may be ints.</span></span><a href="#l1315"></a>
<span id="l1316"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l1316"></a>
<span id="l1317">    <span class="n">__slots__</span> <span class="o">=</span> <span class="n">date</span><span class="o">.</span><span class="n">__slots__</span> <span class="o">+</span> <span class="n">time</span><span class="o">.</span><span class="n">__slots__</span></span><a href="#l1317"></a>
<span id="l1318"></span><a href="#l1318"></a>
<span id="l1319">    <span class="k">def</span> <span class="nf">__new__</span><span class="p">(</span><span class="n">cls</span><span class="p">,</span> <span class="n">year</span><span class="p">,</span> <span class="n">month</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">day</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">hour</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">minute</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">second</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span></span><a href="#l1319"></a>
<span id="l1320">                <span class="n">microsecond</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">tzinfo</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l1320"></a>
<span id="l1321">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">year</span><span class="p">,</span> <span class="nb">bytes</span><span class="p">)</span> <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="n">year</span><span class="p">)</span> <span class="o">==</span> <span class="mi">10</span> <span class="ow">and</span> <span class="mi">1</span> <span class="o">&lt;=</span> <span class="n">year</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span> <span class="o">&lt;=</span> <span class="mi">12</span><span class="p">:</span></span><a href="#l1321"></a>
<span id="l1322">            <span class="c"># Pickle support</span></span><a href="#l1322"></a>
<span id="l1323">            <span class="bp">self</span> <span class="o">=</span> <span class="nb">object</span><span class="o">.</span><span class="n">__new__</span><span class="p">(</span><span class="n">cls</span><span class="p">)</span></span><a href="#l1323"></a>
<span id="l1324">            <span class="bp">self</span><span class="o">.</span><span class="n">__setstate</span><span class="p">(</span><span class="n">year</span><span class="p">,</span> <span class="n">month</span><span class="p">)</span></span><a href="#l1324"></a>
<span id="l1325">            <span class="bp">self</span><span class="o">.</span><span class="n">_hashcode</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span></span><a href="#l1325"></a>
<span id="l1326">            <span class="k">return</span> <span class="bp">self</span></span><a href="#l1326"></a>
<span id="l1327">        <span class="n">year</span><span class="p">,</span> <span class="n">month</span><span class="p">,</span> <span class="n">day</span> <span class="o">=</span> <span class="n">_check_date_fields</span><span class="p">(</span><span class="n">year</span><span class="p">,</span> <span class="n">month</span><span class="p">,</span> <span class="n">day</span><span class="p">)</span></span><a href="#l1327"></a>
<span id="l1328">        <span class="n">hour</span><span class="p">,</span> <span class="n">minute</span><span class="p">,</span> <span class="n">second</span><span class="p">,</span> <span class="n">microsecond</span> <span class="o">=</span> <span class="n">_check_time_fields</span><span class="p">(</span></span><a href="#l1328"></a>
<span id="l1329">            <span class="n">hour</span><span class="p">,</span> <span class="n">minute</span><span class="p">,</span> <span class="n">second</span><span class="p">,</span> <span class="n">microsecond</span><span class="p">)</span></span><a href="#l1329"></a>
<span id="l1330">        <span class="n">_check_tzinfo_arg</span><span class="p">(</span><span class="n">tzinfo</span><span class="p">)</span></span><a href="#l1330"></a>
<span id="l1331">        <span class="bp">self</span> <span class="o">=</span> <span class="nb">object</span><span class="o">.</span><span class="n">__new__</span><span class="p">(</span><span class="n">cls</span><span class="p">)</span></span><a href="#l1331"></a>
<span id="l1332">        <span class="bp">self</span><span class="o">.</span><span class="n">_year</span> <span class="o">=</span> <span class="n">year</span></span><a href="#l1332"></a>
<span id="l1333">        <span class="bp">self</span><span class="o">.</span><span class="n">_month</span> <span class="o">=</span> <span class="n">month</span></span><a href="#l1333"></a>
<span id="l1334">        <span class="bp">self</span><span class="o">.</span><span class="n">_day</span> <span class="o">=</span> <span class="n">day</span></span><a href="#l1334"></a>
<span id="l1335">        <span class="bp">self</span><span class="o">.</span><span class="n">_hour</span> <span class="o">=</span> <span class="n">hour</span></span><a href="#l1335"></a>
<span id="l1336">        <span class="bp">self</span><span class="o">.</span><span class="n">_minute</span> <span class="o">=</span> <span class="n">minute</span></span><a href="#l1336"></a>
<span id="l1337">        <span class="bp">self</span><span class="o">.</span><span class="n">_second</span> <span class="o">=</span> <span class="n">second</span></span><a href="#l1337"></a>
<span id="l1338">        <span class="bp">self</span><span class="o">.</span><span class="n">_microsecond</span> <span class="o">=</span> <span class="n">microsecond</span></span><a href="#l1338"></a>
<span id="l1339">        <span class="bp">self</span><span class="o">.</span><span class="n">_tzinfo</span> <span class="o">=</span> <span class="n">tzinfo</span></span><a href="#l1339"></a>
<span id="l1340">        <span class="bp">self</span><span class="o">.</span><span class="n">_hashcode</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span></span><a href="#l1340"></a>
<span id="l1341">        <span class="k">return</span> <span class="bp">self</span></span><a href="#l1341"></a>
<span id="l1342"></span><a href="#l1342"></a>
<span id="l1343">    <span class="c"># Read-only field accessors</span></span><a href="#l1343"></a>
<span id="l1344">    <span class="nd">@property</span></span><a href="#l1344"></a>
<span id="l1345">    <span class="k">def</span> <span class="nf">hour</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1345"></a>
<span id="l1346">        <span class="sd">&quot;&quot;&quot;hour (0-23)&quot;&quot;&quot;</span></span><a href="#l1346"></a>
<span id="l1347">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_hour</span></span><a href="#l1347"></a>
<span id="l1348"></span><a href="#l1348"></a>
<span id="l1349">    <span class="nd">@property</span></span><a href="#l1349"></a>
<span id="l1350">    <span class="k">def</span> <span class="nf">minute</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1350"></a>
<span id="l1351">        <span class="sd">&quot;&quot;&quot;minute (0-59)&quot;&quot;&quot;</span></span><a href="#l1351"></a>
<span id="l1352">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_minute</span></span><a href="#l1352"></a>
<span id="l1353"></span><a href="#l1353"></a>
<span id="l1354">    <span class="nd">@property</span></span><a href="#l1354"></a>
<span id="l1355">    <span class="k">def</span> <span class="nf">second</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1355"></a>
<span id="l1356">        <span class="sd">&quot;&quot;&quot;second (0-59)&quot;&quot;&quot;</span></span><a href="#l1356"></a>
<span id="l1357">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_second</span></span><a href="#l1357"></a>
<span id="l1358"></span><a href="#l1358"></a>
<span id="l1359">    <span class="nd">@property</span></span><a href="#l1359"></a>
<span id="l1360">    <span class="k">def</span> <span class="nf">microsecond</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1360"></a>
<span id="l1361">        <span class="sd">&quot;&quot;&quot;microsecond (0-999999)&quot;&quot;&quot;</span></span><a href="#l1361"></a>
<span id="l1362">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_microsecond</span></span><a href="#l1362"></a>
<span id="l1363"></span><a href="#l1363"></a>
<span id="l1364">    <span class="nd">@property</span></span><a href="#l1364"></a>
<span id="l1365">    <span class="k">def</span> <span class="nf">tzinfo</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1365"></a>
<span id="l1366">        <span class="sd">&quot;&quot;&quot;timezone info object&quot;&quot;&quot;</span></span><a href="#l1366"></a>
<span id="l1367">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tzinfo</span></span><a href="#l1367"></a>
<span id="l1368"></span><a href="#l1368"></a>
<span id="l1369">    <span class="nd">@classmethod</span></span><a href="#l1369"></a>
<span id="l1370">    <span class="k">def</span> <span class="nf">_fromtimestamp</span><span class="p">(</span><span class="n">cls</span><span class="p">,</span> <span class="n">t</span><span class="p">,</span> <span class="n">utc</span><span class="p">,</span> <span class="n">tz</span><span class="p">):</span></span><a href="#l1370"></a>
<span id="l1371">        <span class="sd">&quot;&quot;&quot;Construct a datetime from a POSIX timestamp (like time.time()).</span></span><a href="#l1371"></a>
<span id="l1372"></span><a href="#l1372"></a>
<span id="l1373"><span class="sd">        A timezone info object may be passed in as well.</span></span><a href="#l1373"></a>
<span id="l1374"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l1374"></a>
<span id="l1375">        <span class="n">frac</span><span class="p">,</span> <span class="n">t</span> <span class="o">=</span> <span class="n">_math</span><span class="o">.</span><span class="n">modf</span><span class="p">(</span><span class="n">t</span><span class="p">)</span></span><a href="#l1375"></a>
<span id="l1376">        <span class="n">us</span> <span class="o">=</span> <span class="nb">round</span><span class="p">(</span><span class="n">frac</span> <span class="o">*</span> <span class="mf">1e6</span><span class="p">)</span></span><a href="#l1376"></a>
<span id="l1377">        <span class="k">if</span> <span class="n">us</span> <span class="o">&gt;=</span> <span class="mi">1000000</span><span class="p">:</span></span><a href="#l1377"></a>
<span id="l1378">            <span class="n">t</span> <span class="o">+=</span> <span class="mi">1</span></span><a href="#l1378"></a>
<span id="l1379">            <span class="n">us</span> <span class="o">-=</span> <span class="mi">1000000</span></span><a href="#l1379"></a>
<span id="l1380">        <span class="k">elif</span> <span class="n">us</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span></span><a href="#l1380"></a>
<span id="l1381">            <span class="n">t</span> <span class="o">-=</span> <span class="mi">1</span></span><a href="#l1381"></a>
<span id="l1382">            <span class="n">us</span> <span class="o">+=</span> <span class="mi">1000000</span></span><a href="#l1382"></a>
<span id="l1383"></span><a href="#l1383"></a>
<span id="l1384">        <span class="n">converter</span> <span class="o">=</span> <span class="n">_time</span><span class="o">.</span><span class="n">gmtime</span> <span class="k">if</span> <span class="n">utc</span> <span class="k">else</span> <span class="n">_time</span><span class="o">.</span><span class="n">localtime</span></span><a href="#l1384"></a>
<span id="l1385">        <span class="n">y</span><span class="p">,</span> <span class="n">m</span><span class="p">,</span> <span class="n">d</span><span class="p">,</span> <span class="n">hh</span><span class="p">,</span> <span class="n">mm</span><span class="p">,</span> <span class="n">ss</span><span class="p">,</span> <span class="n">weekday</span><span class="p">,</span> <span class="n">jday</span><span class="p">,</span> <span class="n">dst</span> <span class="o">=</span> <span class="n">converter</span><span class="p">(</span><span class="n">t</span><span class="p">)</span></span><a href="#l1385"></a>
<span id="l1386">        <span class="n">ss</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="n">ss</span><span class="p">,</span> <span class="mi">59</span><span class="p">)</span>    <span class="c"># clamp out leap seconds if the platform has them</span></span><a href="#l1386"></a>
<span id="l1387">        <span class="k">return</span> <span class="n">cls</span><span class="p">(</span><span class="n">y</span><span class="p">,</span> <span class="n">m</span><span class="p">,</span> <span class="n">d</span><span class="p">,</span> <span class="n">hh</span><span class="p">,</span> <span class="n">mm</span><span class="p">,</span> <span class="n">ss</span><span class="p">,</span> <span class="n">us</span><span class="p">,</span> <span class="n">tz</span><span class="p">)</span></span><a href="#l1387"></a>
<span id="l1388"></span><a href="#l1388"></a>
<span id="l1389">    <span class="nd">@classmethod</span></span><a href="#l1389"></a>
<span id="l1390">    <span class="k">def</span> <span class="nf">fromtimestamp</span><span class="p">(</span><span class="n">cls</span><span class="p">,</span> <span class="n">t</span><span class="p">,</span> <span class="n">tz</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l1390"></a>
<span id="l1391">        <span class="sd">&quot;&quot;&quot;Construct a datetime from a POSIX timestamp (like time.time()).</span></span><a href="#l1391"></a>
<span id="l1392"></span><a href="#l1392"></a>
<span id="l1393"><span class="sd">        A timezone info object may be passed in as well.</span></span><a href="#l1393"></a>
<span id="l1394"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l1394"></a>
<span id="l1395">        <span class="n">_check_tzinfo_arg</span><span class="p">(</span><span class="n">tz</span><span class="p">)</span></span><a href="#l1395"></a>
<span id="l1396"></span><a href="#l1396"></a>
<span id="l1397">        <span class="n">result</span> <span class="o">=</span> <span class="n">cls</span><span class="o">.</span><span class="n">_fromtimestamp</span><span class="p">(</span><span class="n">t</span><span class="p">,</span> <span class="n">tz</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">,</span> <span class="n">tz</span><span class="p">)</span></span><a href="#l1397"></a>
<span id="l1398">        <span class="k">if</span> <span class="n">tz</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1398"></a>
<span id="l1399">            <span class="n">result</span> <span class="o">=</span> <span class="n">tz</span><span class="o">.</span><span class="n">fromutc</span><span class="p">(</span><span class="n">result</span><span class="p">)</span></span><a href="#l1399"></a>
<span id="l1400">        <span class="k">return</span> <span class="n">result</span></span><a href="#l1400"></a>
<span id="l1401"></span><a href="#l1401"></a>
<span id="l1402">    <span class="nd">@classmethod</span></span><a href="#l1402"></a>
<span id="l1403">    <span class="k">def</span> <span class="nf">utcfromtimestamp</span><span class="p">(</span><span class="n">cls</span><span class="p">,</span> <span class="n">t</span><span class="p">):</span></span><a href="#l1403"></a>
<span id="l1404">        <span class="sd">&quot;&quot;&quot;Construct a naive UTC datetime from a POSIX timestamp.&quot;&quot;&quot;</span></span><a href="#l1404"></a>
<span id="l1405">        <span class="k">return</span> <span class="n">cls</span><span class="o">.</span><span class="n">_fromtimestamp</span><span class="p">(</span><span class="n">t</span><span class="p">,</span> <span class="bp">True</span><span class="p">,</span> <span class="bp">None</span><span class="p">)</span></span><a href="#l1405"></a>
<span id="l1406"></span><a href="#l1406"></a>
<span id="l1407">    <span class="nd">@classmethod</span></span><a href="#l1407"></a>
<span id="l1408">    <span class="k">def</span> <span class="nf">now</span><span class="p">(</span><span class="n">cls</span><span class="p">,</span> <span class="n">tz</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l1408"></a>
<span id="l1409">        <span class="s">&quot;Construct a datetime from time.time() and optional time zone info.&quot;</span></span><a href="#l1409"></a>
<span id="l1410">        <span class="n">t</span> <span class="o">=</span> <span class="n">_time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span></span><a href="#l1410"></a>
<span id="l1411">        <span class="k">return</span> <span class="n">cls</span><span class="o">.</span><span class="n">fromtimestamp</span><span class="p">(</span><span class="n">t</span><span class="p">,</span> <span class="n">tz</span><span class="p">)</span></span><a href="#l1411"></a>
<span id="l1412"></span><a href="#l1412"></a>
<span id="l1413">    <span class="nd">@classmethod</span></span><a href="#l1413"></a>
<span id="l1414">    <span class="k">def</span> <span class="nf">utcnow</span><span class="p">(</span><span class="n">cls</span><span class="p">):</span></span><a href="#l1414"></a>
<span id="l1415">        <span class="s">&quot;Construct a UTC datetime from time.time().&quot;</span></span><a href="#l1415"></a>
<span id="l1416">        <span class="n">t</span> <span class="o">=</span> <span class="n">_time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span></span><a href="#l1416"></a>
<span id="l1417">        <span class="k">return</span> <span class="n">cls</span><span class="o">.</span><span class="n">utcfromtimestamp</span><span class="p">(</span><span class="n">t</span><span class="p">)</span></span><a href="#l1417"></a>
<span id="l1418"></span><a href="#l1418"></a>
<span id="l1419">    <span class="nd">@classmethod</span></span><a href="#l1419"></a>
<span id="l1420">    <span class="k">def</span> <span class="nf">combine</span><span class="p">(</span><span class="n">cls</span><span class="p">,</span> <span class="n">date</span><span class="p">,</span> <span class="n">time</span><span class="p">):</span></span><a href="#l1420"></a>
<span id="l1421">        <span class="s">&quot;Construct a datetime from a given date and a given time.&quot;</span></span><a href="#l1421"></a>
<span id="l1422">        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">date</span><span class="p">,</span> <span class="n">_date_class</span><span class="p">):</span></span><a href="#l1422"></a>
<span id="l1423">            <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="s">&quot;date argument must be a date instance&quot;</span><span class="p">)</span></span><a href="#l1423"></a>
<span id="l1424">        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">time</span><span class="p">,</span> <span class="n">_time_class</span><span class="p">):</span></span><a href="#l1424"></a>
<span id="l1425">            <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="s">&quot;time argument must be a time instance&quot;</span><span class="p">)</span></span><a href="#l1425"></a>
<span id="l1426">        <span class="k">return</span> <span class="n">cls</span><span class="p">(</span><span class="n">date</span><span class="o">.</span><span class="n">year</span><span class="p">,</span> <span class="n">date</span><span class="o">.</span><span class="n">month</span><span class="p">,</span> <span class="n">date</span><span class="o">.</span><span class="n">day</span><span class="p">,</span></span><a href="#l1426"></a>
<span id="l1427">                   <span class="n">time</span><span class="o">.</span><span class="n">hour</span><span class="p">,</span> <span class="n">time</span><span class="o">.</span><span class="n">minute</span><span class="p">,</span> <span class="n">time</span><span class="o">.</span><span class="n">second</span><span class="p">,</span> <span class="n">time</span><span class="o">.</span><span class="n">microsecond</span><span class="p">,</span></span><a href="#l1427"></a>
<span id="l1428">                   <span class="n">time</span><span class="o">.</span><span class="n">tzinfo</span><span class="p">)</span></span><a href="#l1428"></a>
<span id="l1429"></span><a href="#l1429"></a>
<span id="l1430">    <span class="k">def</span> <span class="nf">timetuple</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1430"></a>
<span id="l1431">        <span class="s">&quot;Return local time tuple compatible with time.localtime().&quot;</span></span><a href="#l1431"></a>
<span id="l1432">        <span class="n">dst</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">dst</span><span class="p">()</span></span><a href="#l1432"></a>
<span id="l1433">        <span class="k">if</span> <span class="n">dst</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1433"></a>
<span id="l1434">            <span class="n">dst</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span></span><a href="#l1434"></a>
<span id="l1435">        <span class="k">elif</span> <span class="n">dst</span><span class="p">:</span></span><a href="#l1435"></a>
<span id="l1436">            <span class="n">dst</span> <span class="o">=</span> <span class="mi">1</span></span><a href="#l1436"></a>
<span id="l1437">        <span class="k">else</span><span class="p">:</span></span><a href="#l1437"></a>
<span id="l1438">            <span class="n">dst</span> <span class="o">=</span> <span class="mi">0</span></span><a href="#l1438"></a>
<span id="l1439">        <span class="k">return</span> <span class="n">_build_struct_time</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">year</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">month</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">day</span><span class="p">,</span></span><a href="#l1439"></a>
<span id="l1440">                                  <span class="bp">self</span><span class="o">.</span><span class="n">hour</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">minute</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">second</span><span class="p">,</span></span><a href="#l1440"></a>
<span id="l1441">                                  <span class="n">dst</span><span class="p">)</span></span><a href="#l1441"></a>
<span id="l1442"></span><a href="#l1442"></a>
<span id="l1443">    <span class="k">def</span> <span class="nf">timestamp</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1443"></a>
<span id="l1444">        <span class="s">&quot;Return POSIX timestamp as float&quot;</span></span><a href="#l1444"></a>
<span id="l1445">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tzinfo</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1445"></a>
<span id="l1446">            <span class="k">return</span> <span class="n">_time</span><span class="o">.</span><span class="n">mktime</span><span class="p">((</span><span class="bp">self</span><span class="o">.</span><span class="n">year</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">month</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">day</span><span class="p">,</span></span><a href="#l1446"></a>
<span id="l1447">                                 <span class="bp">self</span><span class="o">.</span><span class="n">hour</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">minute</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">second</span><span class="p">,</span></span><a href="#l1447"></a>
<span id="l1448">                                 <span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">))</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">microsecond</span> <span class="o">/</span> <span class="mf">1e6</span></span><a href="#l1448"></a>
<span id="l1449">        <span class="k">else</span><span class="p">:</span></span><a href="#l1449"></a>
<span id="l1450">            <span class="k">return</span> <span class="p">(</span><span class="bp">self</span> <span class="o">-</span> <span class="n">_EPOCH</span><span class="p">)</span><span class="o">.</span><span class="n">total_seconds</span><span class="p">()</span></span><a href="#l1450"></a>
<span id="l1451"></span><a href="#l1451"></a>
<span id="l1452">    <span class="k">def</span> <span class="nf">utctimetuple</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1452"></a>
<span id="l1453">        <span class="s">&quot;Return UTC time tuple compatible with time.gmtime().&quot;</span></span><a href="#l1453"></a>
<span id="l1454">        <span class="n">offset</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">utcoffset</span><span class="p">()</span></span><a href="#l1454"></a>
<span id="l1455">        <span class="k">if</span> <span class="n">offset</span><span class="p">:</span></span><a href="#l1455"></a>
<span id="l1456">            <span class="bp">self</span> <span class="o">-=</span> <span class="n">offset</span></span><a href="#l1456"></a>
<span id="l1457">        <span class="n">y</span><span class="p">,</span> <span class="n">m</span><span class="p">,</span> <span class="n">d</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">year</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">month</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">day</span></span><a href="#l1457"></a>
<span id="l1458">        <span class="n">hh</span><span class="p">,</span> <span class="n">mm</span><span class="p">,</span> <span class="n">ss</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">hour</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">minute</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">second</span></span><a href="#l1458"></a>
<span id="l1459">        <span class="k">return</span> <span class="n">_build_struct_time</span><span class="p">(</span><span class="n">y</span><span class="p">,</span> <span class="n">m</span><span class="p">,</span> <span class="n">d</span><span class="p">,</span> <span class="n">hh</span><span class="p">,</span> <span class="n">mm</span><span class="p">,</span> <span class="n">ss</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span></span><a href="#l1459"></a>
<span id="l1460"></span><a href="#l1460"></a>
<span id="l1461">    <span class="k">def</span> <span class="nf">date</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1461"></a>
<span id="l1462">        <span class="s">&quot;Return the date part.&quot;</span></span><a href="#l1462"></a>
<span id="l1463">        <span class="k">return</span> <span class="n">date</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_year</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_month</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_day</span><span class="p">)</span></span><a href="#l1463"></a>
<span id="l1464"></span><a href="#l1464"></a>
<span id="l1465">    <span class="k">def</span> <span class="nf">time</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1465"></a>
<span id="l1466">        <span class="s">&quot;Return the time part, with tzinfo None.&quot;</span></span><a href="#l1466"></a>
<span id="l1467">        <span class="k">return</span> <span class="n">time</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">hour</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">minute</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">second</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">microsecond</span><span class="p">)</span></span><a href="#l1467"></a>
<span id="l1468"></span><a href="#l1468"></a>
<span id="l1469">    <span class="k">def</span> <span class="nf">timetz</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1469"></a>
<span id="l1470">        <span class="s">&quot;Return the time part, with same tzinfo.&quot;</span></span><a href="#l1470"></a>
<span id="l1471">        <span class="k">return</span> <span class="n">time</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">hour</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">minute</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">second</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">microsecond</span><span class="p">,</span></span><a href="#l1471"></a>
<span id="l1472">                    <span class="bp">self</span><span class="o">.</span><span class="n">_tzinfo</span><span class="p">)</span></span><a href="#l1472"></a>
<span id="l1473"></span><a href="#l1473"></a>
<span id="l1474">    <span class="k">def</span> <span class="nf">replace</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">year</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">month</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">day</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">hour</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span></span><a href="#l1474"></a>
<span id="l1475">                <span class="n">minute</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">second</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">microsecond</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">tzinfo</span><span class="o">=</span><span class="bp">True</span><span class="p">):</span></span><a href="#l1475"></a>
<span id="l1476">        <span class="sd">&quot;&quot;&quot;Return a new datetime with new values for the specified fields.&quot;&quot;&quot;</span></span><a href="#l1476"></a>
<span id="l1477">        <span class="k">if</span> <span class="n">year</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1477"></a>
<span id="l1478">            <span class="n">year</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">year</span></span><a href="#l1478"></a>
<span id="l1479">        <span class="k">if</span> <span class="n">month</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1479"></a>
<span id="l1480">            <span class="n">month</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">month</span></span><a href="#l1480"></a>
<span id="l1481">        <span class="k">if</span> <span class="n">day</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1481"></a>
<span id="l1482">            <span class="n">day</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">day</span></span><a href="#l1482"></a>
<span id="l1483">        <span class="k">if</span> <span class="n">hour</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1483"></a>
<span id="l1484">            <span class="n">hour</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">hour</span></span><a href="#l1484"></a>
<span id="l1485">        <span class="k">if</span> <span class="n">minute</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1485"></a>
<span id="l1486">            <span class="n">minute</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">minute</span></span><a href="#l1486"></a>
<span id="l1487">        <span class="k">if</span> <span class="n">second</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1487"></a>
<span id="l1488">            <span class="n">second</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">second</span></span><a href="#l1488"></a>
<span id="l1489">        <span class="k">if</span> <span class="n">microsecond</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1489"></a>
<span id="l1490">            <span class="n">microsecond</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">microsecond</span></span><a href="#l1490"></a>
<span id="l1491">        <span class="k">if</span> <span class="n">tzinfo</span> <span class="ow">is</span> <span class="bp">True</span><span class="p">:</span></span><a href="#l1491"></a>
<span id="l1492">            <span class="n">tzinfo</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tzinfo</span></span><a href="#l1492"></a>
<span id="l1493">        <span class="k">return</span> <span class="n">datetime</span><span class="p">(</span><span class="n">year</span><span class="p">,</span> <span class="n">month</span><span class="p">,</span> <span class="n">day</span><span class="p">,</span> <span class="n">hour</span><span class="p">,</span> <span class="n">minute</span><span class="p">,</span> <span class="n">second</span><span class="p">,</span> <span class="n">microsecond</span><span class="p">,</span></span><a href="#l1493"></a>
<span id="l1494">                        <span class="n">tzinfo</span><span class="p">)</span></span><a href="#l1494"></a>
<span id="l1495"></span><a href="#l1495"></a>
<span id="l1496">    <span class="k">def</span> <span class="nf">astimezone</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tz</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l1496"></a>
<span id="l1497">        <span class="k">if</span> <span class="n">tz</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1497"></a>
<span id="l1498">            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">tzinfo</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1498"></a>
<span id="l1499">                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&quot;astimezone() requires an aware datetime&quot;</span><span class="p">)</span></span><a href="#l1499"></a>
<span id="l1500">            <span class="n">ts</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span> <span class="o">-</span> <span class="n">_EPOCH</span><span class="p">)</span> <span class="o">//</span> <span class="n">timedelta</span><span class="p">(</span><span class="n">seconds</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span></span><a href="#l1500"></a>
<span id="l1501">            <span class="n">localtm</span> <span class="o">=</span> <span class="n">_time</span><span class="o">.</span><span class="n">localtime</span><span class="p">(</span><span class="n">ts</span><span class="p">)</span></span><a href="#l1501"></a>
<span id="l1502">            <span class="n">local</span> <span class="o">=</span> <span class="n">datetime</span><span class="p">(</span><span class="o">*</span><span class="n">localtm</span><span class="p">[:</span><span class="mi">6</span><span class="p">])</span></span><a href="#l1502"></a>
<span id="l1503">            <span class="k">try</span><span class="p">:</span></span><a href="#l1503"></a>
<span id="l1504">                <span class="c"># Extract TZ data if available</span></span><a href="#l1504"></a>
<span id="l1505">                <span class="n">gmtoff</span> <span class="o">=</span> <span class="n">localtm</span><span class="o">.</span><span class="n">tm_gmtoff</span></span><a href="#l1505"></a>
<span id="l1506">                <span class="n">zone</span> <span class="o">=</span> <span class="n">localtm</span><span class="o">.</span><span class="n">tm_zone</span></span><a href="#l1506"></a>
<span id="l1507">            <span class="k">except</span> <span class="ne">AttributeError</span><span class="p">:</span></span><a href="#l1507"></a>
<span id="l1508">                <span class="c"># Compute UTC offset and compare with the value implied</span></span><a href="#l1508"></a>
<span id="l1509">                <span class="c"># by tm_isdst.  If the values match, use the zone name</span></span><a href="#l1509"></a>
<span id="l1510">                <span class="c"># implied by tm_isdst.</span></span><a href="#l1510"></a>
<span id="l1511">                <span class="n">delta</span> <span class="o">=</span> <span class="n">local</span> <span class="o">-</span> <span class="n">datetime</span><span class="p">(</span><span class="o">*</span><span class="n">_time</span><span class="o">.</span><span class="n">gmtime</span><span class="p">(</span><span class="n">ts</span><span class="p">)[:</span><span class="mi">6</span><span class="p">])</span></span><a href="#l1511"></a>
<span id="l1512">                <span class="n">dst</span> <span class="o">=</span> <span class="n">_time</span><span class="o">.</span><span class="n">daylight</span> <span class="ow">and</span> <span class="n">localtm</span><span class="o">.</span><span class="n">tm_isdst</span> <span class="o">&gt;</span> <span class="mi">0</span></span><a href="#l1512"></a>
<span id="l1513">                <span class="n">gmtoff</span> <span class="o">=</span> <span class="o">-</span><span class="p">(</span><span class="n">_time</span><span class="o">.</span><span class="n">altzone</span> <span class="k">if</span> <span class="n">dst</span> <span class="k">else</span> <span class="n">_time</span><span class="o">.</span><span class="n">timezone</span><span class="p">)</span></span><a href="#l1513"></a>
<span id="l1514">                <span class="k">if</span> <span class="n">delta</span> <span class="o">==</span> <span class="n">timedelta</span><span class="p">(</span><span class="n">seconds</span><span class="o">=</span><span class="n">gmtoff</span><span class="p">):</span></span><a href="#l1514"></a>
<span id="l1515">                    <span class="n">tz</span> <span class="o">=</span> <span class="n">timezone</span><span class="p">(</span><span class="n">delta</span><span class="p">,</span> <span class="n">_time</span><span class="o">.</span><span class="n">tzname</span><span class="p">[</span><span class="n">dst</span><span class="p">])</span></span><a href="#l1515"></a>
<span id="l1516">                <span class="k">else</span><span class="p">:</span></span><a href="#l1516"></a>
<span id="l1517">                    <span class="n">tz</span> <span class="o">=</span> <span class="n">timezone</span><span class="p">(</span><span class="n">delta</span><span class="p">)</span></span><a href="#l1517"></a>
<span id="l1518">            <span class="k">else</span><span class="p">:</span></span><a href="#l1518"></a>
<span id="l1519">                <span class="n">tz</span> <span class="o">=</span> <span class="n">timezone</span><span class="p">(</span><span class="n">timedelta</span><span class="p">(</span><span class="n">seconds</span><span class="o">=</span><span class="n">gmtoff</span><span class="p">),</span> <span class="n">zone</span><span class="p">)</span></span><a href="#l1519"></a>
<span id="l1520"></span><a href="#l1520"></a>
<span id="l1521">        <span class="k">elif</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">tz</span><span class="p">,</span> <span class="n">tzinfo</span><span class="p">):</span></span><a href="#l1521"></a>
<span id="l1522">            <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="s">&quot;tz argument must be an instance of tzinfo&quot;</span><span class="p">)</span></span><a href="#l1522"></a>
<span id="l1523"></span><a href="#l1523"></a>
<span id="l1524">        <span class="n">mytz</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">tzinfo</span></span><a href="#l1524"></a>
<span id="l1525">        <span class="k">if</span> <span class="n">mytz</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1525"></a>
<span id="l1526">            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&quot;astimezone() requires an aware datetime&quot;</span><span class="p">)</span></span><a href="#l1526"></a>
<span id="l1527"></span><a href="#l1527"></a>
<span id="l1528">        <span class="k">if</span> <span class="n">tz</span> <span class="ow">is</span> <span class="n">mytz</span><span class="p">:</span></span><a href="#l1528"></a>
<span id="l1529">            <span class="k">return</span> <span class="bp">self</span></span><a href="#l1529"></a>
<span id="l1530"></span><a href="#l1530"></a>
<span id="l1531">        <span class="c"># Convert self to UTC, and attach the new time zone object.</span></span><a href="#l1531"></a>
<span id="l1532">        <span class="n">myoffset</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">utcoffset</span><span class="p">()</span></span><a href="#l1532"></a>
<span id="l1533">        <span class="k">if</span> <span class="n">myoffset</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1533"></a>
<span id="l1534">            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&quot;astimezone() requires an aware datetime&quot;</span><span class="p">)</span></span><a href="#l1534"></a>
<span id="l1535">        <span class="n">utc</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span> <span class="o">-</span> <span class="n">myoffset</span><span class="p">)</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="n">tzinfo</span><span class="o">=</span><span class="n">tz</span><span class="p">)</span></span><a href="#l1535"></a>
<span id="l1536"></span><a href="#l1536"></a>
<span id="l1537">        <span class="c"># Convert from UTC to tz&#39;s local time.</span></span><a href="#l1537"></a>
<span id="l1538">        <span class="k">return</span> <span class="n">tz</span><span class="o">.</span><span class="n">fromutc</span><span class="p">(</span><span class="n">utc</span><span class="p">)</span></span><a href="#l1538"></a>
<span id="l1539"></span><a href="#l1539"></a>
<span id="l1540">    <span class="c"># Ways to produce a string.</span></span><a href="#l1540"></a>
<span id="l1541"></span><a href="#l1541"></a>
<span id="l1542">    <span class="k">def</span> <span class="nf">ctime</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1542"></a>
<span id="l1543">        <span class="s">&quot;Return ctime() style string.&quot;</span></span><a href="#l1543"></a>
<span id="l1544">        <span class="n">weekday</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">toordinal</span><span class="p">()</span> <span class="o">%</span> <span class="mi">7</span> <span class="ow">or</span> <span class="mi">7</span></span><a href="#l1544"></a>
<span id="l1545">        <span class="k">return</span> <span class="s">&quot;</span><span class="si">%s</span><span class="s"> </span><span class="si">%s</span><span class="s"> </span><span class="si">%2d</span><span class="s"> </span><span class="si">%02d</span><span class="s">:</span><span class="si">%02d</span><span class="s">:</span><span class="si">%02d</span><span class="s"> </span><span class="si">%04d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span></span><a href="#l1545"></a>
<span id="l1546">            <span class="n">_DAYNAMES</span><span class="p">[</span><span class="n">weekday</span><span class="p">],</span></span><a href="#l1546"></a>
<span id="l1547">            <span class="n">_MONTHNAMES</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_month</span><span class="p">],</span></span><a href="#l1547"></a>
<span id="l1548">            <span class="bp">self</span><span class="o">.</span><span class="n">_day</span><span class="p">,</span></span><a href="#l1548"></a>
<span id="l1549">            <span class="bp">self</span><span class="o">.</span><span class="n">_hour</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_minute</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_second</span><span class="p">,</span></span><a href="#l1549"></a>
<span id="l1550">            <span class="bp">self</span><span class="o">.</span><span class="n">_year</span><span class="p">)</span></span><a href="#l1550"></a>
<span id="l1551"></span><a href="#l1551"></a>
<span id="l1552">    <span class="k">def</span> <span class="nf">isoformat</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">sep</span><span class="o">=</span><span class="s">&#39;T&#39;</span><span class="p">):</span></span><a href="#l1552"></a>
<span id="l1553">        <span class="sd">&quot;&quot;&quot;Return the time formatted according to ISO.</span></span><a href="#l1553"></a>
<span id="l1554"></span><a href="#l1554"></a>
<span id="l1555"><span class="sd">        This is &#39;YYYY-MM-DD HH:MM:SS.mmmmmm&#39;, or &#39;YYYY-MM-DD HH:MM:SS&#39; if</span></span><a href="#l1555"></a>
<span id="l1556"><span class="sd">        self.microsecond == 0.</span></span><a href="#l1556"></a>
<span id="l1557"></span><a href="#l1557"></a>
<span id="l1558"><span class="sd">        If self.tzinfo is not None, the UTC offset is also attached, giving</span></span><a href="#l1558"></a>
<span id="l1559"><span class="sd">        &#39;YYYY-MM-DD HH:MM:SS.mmmmmm+HH:MM&#39; or &#39;YYYY-MM-DD HH:MM:SS+HH:MM&#39;.</span></span><a href="#l1559"></a>
<span id="l1560"></span><a href="#l1560"></a>
<span id="l1561"><span class="sd">        Optional argument sep specifies the separator between date and</span></span><a href="#l1561"></a>
<span id="l1562"><span class="sd">        time, default &#39;T&#39;.</span></span><a href="#l1562"></a>
<span id="l1563"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l1563"></a>
<span id="l1564">        <span class="n">s</span> <span class="o">=</span> <span class="p">(</span><span class="s">&quot;</span><span class="si">%04d</span><span class="s">-</span><span class="si">%02d</span><span class="s">-</span><span class="si">%02d%c</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_year</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_month</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_day</span><span class="p">,</span> <span class="n">sep</span><span class="p">)</span> <span class="o">+</span></span><a href="#l1564"></a>
<span id="l1565">             <span class="n">_format_time</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_hour</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_minute</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_second</span><span class="p">,</span></span><a href="#l1565"></a>
<span id="l1566">                          <span class="bp">self</span><span class="o">.</span><span class="n">_microsecond</span><span class="p">))</span></span><a href="#l1566"></a>
<span id="l1567">        <span class="n">off</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">utcoffset</span><span class="p">()</span></span><a href="#l1567"></a>
<span id="l1568">        <span class="k">if</span> <span class="n">off</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1568"></a>
<span id="l1569">            <span class="k">if</span> <span class="n">off</span><span class="o">.</span><span class="n">days</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span></span><a href="#l1569"></a>
<span id="l1570">                <span class="n">sign</span> <span class="o">=</span> <span class="s">&quot;-&quot;</span></span><a href="#l1570"></a>
<span id="l1571">                <span class="n">off</span> <span class="o">=</span> <span class="o">-</span><span class="n">off</span></span><a href="#l1571"></a>
<span id="l1572">            <span class="k">else</span><span class="p">:</span></span><a href="#l1572"></a>
<span id="l1573">                <span class="n">sign</span> <span class="o">=</span> <span class="s">&quot;+&quot;</span></span><a href="#l1573"></a>
<span id="l1574">            <span class="n">hh</span><span class="p">,</span> <span class="n">mm</span> <span class="o">=</span> <span class="nb">divmod</span><span class="p">(</span><span class="n">off</span><span class="p">,</span> <span class="n">timedelta</span><span class="p">(</span><span class="n">hours</span><span class="o">=</span><span class="mi">1</span><span class="p">))</span></span><a href="#l1574"></a>
<span id="l1575">            <span class="k">assert</span> <span class="ow">not</span> <span class="n">mm</span> <span class="o">%</span> <span class="n">timedelta</span><span class="p">(</span><span class="n">minutes</span><span class="o">=</span><span class="mi">1</span><span class="p">),</span> <span class="s">&quot;whole minute&quot;</span></span><a href="#l1575"></a>
<span id="l1576">            <span class="n">mm</span> <span class="o">//=</span> <span class="n">timedelta</span><span class="p">(</span><span class="n">minutes</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span></span><a href="#l1576"></a>
<span id="l1577">            <span class="n">s</span> <span class="o">+=</span> <span class="s">&quot;</span><span class="si">%s%02d</span><span class="s">:</span><span class="si">%02d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">sign</span><span class="p">,</span> <span class="n">hh</span><span class="p">,</span> <span class="n">mm</span><span class="p">)</span></span><a href="#l1577"></a>
<span id="l1578">        <span class="k">return</span> <span class="n">s</span></span><a href="#l1578"></a>
<span id="l1579"></span><a href="#l1579"></a>
<span id="l1580">    <span class="k">def</span> <span class="nf">__repr__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1580"></a>
<span id="l1581">        <span class="sd">&quot;&quot;&quot;Convert to formal string, for repr().&quot;&quot;&quot;</span></span><a href="#l1581"></a>
<span id="l1582">        <span class="n">L</span> <span class="o">=</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">_year</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_month</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_day</span><span class="p">,</span>  <span class="c"># These are never zero</span></span><a href="#l1582"></a>
<span id="l1583">             <span class="bp">self</span><span class="o">.</span><span class="n">_hour</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_minute</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_second</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_microsecond</span><span class="p">]</span></span><a href="#l1583"></a>
<span id="l1584">        <span class="k">if</span> <span class="n">L</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span></span><a href="#l1584"></a>
<span id="l1585">            <span class="k">del</span> <span class="n">L</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span></span><a href="#l1585"></a>
<span id="l1586">        <span class="k">if</span> <span class="n">L</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span></span><a href="#l1586"></a>
<span id="l1587">            <span class="k">del</span> <span class="n">L</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span></span><a href="#l1587"></a>
<span id="l1588">        <span class="n">s</span> <span class="o">=</span> <span class="s">&quot;</span><span class="si">%s</span><span class="s">.</span><span class="si">%s</span><span class="s">(</span><span class="si">%s</span><span class="s">)&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__class__</span><span class="o">.</span><span class="n">__module__</span><span class="p">,</span></span><a href="#l1588"></a>
<span id="l1589">                           <span class="bp">self</span><span class="o">.</span><span class="n">__class__</span><span class="o">.</span><span class="n">__qualname__</span><span class="p">,</span></span><a href="#l1589"></a>
<span id="l1590">                           <span class="s">&quot;, &quot;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="nb">map</span><span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="n">L</span><span class="p">)))</span></span><a href="#l1590"></a>
<span id="l1591">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tzinfo</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1591"></a>
<span id="l1592">            <span class="k">assert</span> <span class="n">s</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">:]</span> <span class="o">==</span> <span class="s">&quot;)&quot;</span></span><a href="#l1592"></a>
<span id="l1593">            <span class="n">s</span> <span class="o">=</span> <span class="n">s</span><span class="p">[:</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span> <span class="o">+</span> <span class="s">&quot;, tzinfo=</span><span class="si">%r</span><span class="s">&quot;</span> <span class="o">%</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tzinfo</span> <span class="o">+</span> <span class="s">&quot;)&quot;</span></span><a href="#l1593"></a>
<span id="l1594">        <span class="k">return</span> <span class="n">s</span></span><a href="#l1594"></a>
<span id="l1595"></span><a href="#l1595"></a>
<span id="l1596">    <span class="k">def</span> <span class="nf">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1596"></a>
<span id="l1597">        <span class="s">&quot;Convert to string, for str().&quot;</span></span><a href="#l1597"></a>
<span id="l1598">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">isoformat</span><span class="p">(</span><span class="n">sep</span><span class="o">=</span><span class="s">&#39; &#39;</span><span class="p">)</span></span><a href="#l1598"></a>
<span id="l1599"></span><a href="#l1599"></a>
<span id="l1600">    <span class="nd">@classmethod</span></span><a href="#l1600"></a>
<span id="l1601">    <span class="k">def</span> <span class="nf">strptime</span><span class="p">(</span><span class="n">cls</span><span class="p">,</span> <span class="n">date_string</span><span class="p">,</span> <span class="n">format</span><span class="p">):</span></span><a href="#l1601"></a>
<span id="l1602">        <span class="s">&#39;string, format -&gt; new datetime parsed from a string (like time.strptime()).&#39;</span></span><a href="#l1602"></a>
<span id="l1603">        <span class="kn">import</span> <span class="nn">_strptime</span></span><a href="#l1603"></a>
<span id="l1604">        <span class="k">return</span> <span class="n">_strptime</span><span class="o">.</span><span class="n">_strptime_datetime</span><span class="p">(</span><span class="n">cls</span><span class="p">,</span> <span class="n">date_string</span><span class="p">,</span> <span class="n">format</span><span class="p">)</span></span><a href="#l1604"></a>
<span id="l1605"></span><a href="#l1605"></a>
<span id="l1606">    <span class="k">def</span> <span class="nf">utcoffset</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1606"></a>
<span id="l1607">        <span class="sd">&quot;&quot;&quot;Return the timezone offset in minutes east of UTC (negative west of</span></span><a href="#l1607"></a>
<span id="l1608"><span class="sd">        UTC).&quot;&quot;&quot;</span></span><a href="#l1608"></a>
<span id="l1609">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tzinfo</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1609"></a>
<span id="l1610">            <span class="k">return</span> <span class="bp">None</span></span><a href="#l1610"></a>
<span id="l1611">        <span class="n">offset</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tzinfo</span><span class="o">.</span><span class="n">utcoffset</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span></span><a href="#l1611"></a>
<span id="l1612">        <span class="n">_check_utc_offset</span><span class="p">(</span><span class="s">&quot;utcoffset&quot;</span><span class="p">,</span> <span class="n">offset</span><span class="p">)</span></span><a href="#l1612"></a>
<span id="l1613">        <span class="k">return</span> <span class="n">offset</span></span><a href="#l1613"></a>
<span id="l1614"></span><a href="#l1614"></a>
<span id="l1615">    <span class="k">def</span> <span class="nf">tzname</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1615"></a>
<span id="l1616">        <span class="sd">&quot;&quot;&quot;Return the timezone name.</span></span><a href="#l1616"></a>
<span id="l1617"></span><a href="#l1617"></a>
<span id="l1618"><span class="sd">        Note that the name is 100% informational -- there&#39;s no requirement that</span></span><a href="#l1618"></a>
<span id="l1619"><span class="sd">        it mean anything in particular. For example, &quot;GMT&quot;, &quot;UTC&quot;, &quot;-500&quot;,</span></span><a href="#l1619"></a>
<span id="l1620"><span class="sd">        &quot;-5:00&quot;, &quot;EDT&quot;, &quot;US/Eastern&quot;, &quot;America/New York&quot; are all valid replies.</span></span><a href="#l1620"></a>
<span id="l1621"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l1621"></a>
<span id="l1622">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tzinfo</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1622"></a>
<span id="l1623">            <span class="k">return</span> <span class="bp">None</span></span><a href="#l1623"></a>
<span id="l1624">        <span class="n">name</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tzinfo</span><span class="o">.</span><span class="n">tzname</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span></span><a href="#l1624"></a>
<span id="l1625">        <span class="n">_check_tzname</span><span class="p">(</span><span class="n">name</span><span class="p">)</span></span><a href="#l1625"></a>
<span id="l1626">        <span class="k">return</span> <span class="n">name</span></span><a href="#l1626"></a>
<span id="l1627"></span><a href="#l1627"></a>
<span id="l1628">    <span class="k">def</span> <span class="nf">dst</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1628"></a>
<span id="l1629">        <span class="sd">&quot;&quot;&quot;Return 0 if DST is not in effect, or the DST offset (in minutes</span></span><a href="#l1629"></a>
<span id="l1630"><span class="sd">        eastward) if DST is in effect.</span></span><a href="#l1630"></a>
<span id="l1631"></span><a href="#l1631"></a>
<span id="l1632"><span class="sd">        This is purely informational; the DST offset has already been added to</span></span><a href="#l1632"></a>
<span id="l1633"><span class="sd">        the UTC offset returned by utcoffset() if applicable, so there&#39;s no</span></span><a href="#l1633"></a>
<span id="l1634"><span class="sd">        need to consult dst() unless you&#39;re interested in displaying the DST</span></span><a href="#l1634"></a>
<span id="l1635"><span class="sd">        info.</span></span><a href="#l1635"></a>
<span id="l1636"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l1636"></a>
<span id="l1637">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tzinfo</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1637"></a>
<span id="l1638">            <span class="k">return</span> <span class="bp">None</span></span><a href="#l1638"></a>
<span id="l1639">        <span class="n">offset</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tzinfo</span><span class="o">.</span><span class="n">dst</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span></span><a href="#l1639"></a>
<span id="l1640">        <span class="n">_check_utc_offset</span><span class="p">(</span><span class="s">&quot;dst&quot;</span><span class="p">,</span> <span class="n">offset</span><span class="p">)</span></span><a href="#l1640"></a>
<span id="l1641">        <span class="k">return</span> <span class="n">offset</span></span><a href="#l1641"></a>
<span id="l1642"></span><a href="#l1642"></a>
<span id="l1643">    <span class="c"># Comparisons of datetime objects with other.</span></span><a href="#l1643"></a>
<span id="l1644"></span><a href="#l1644"></a>
<span id="l1645">    <span class="k">def</span> <span class="nf">__eq__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l1645"></a>
<span id="l1646">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">datetime</span><span class="p">):</span></span><a href="#l1646"></a>
<span id="l1647">            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cmp</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">allow_mixed</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span></span><a href="#l1647"></a>
<span id="l1648">        <span class="k">elif</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">date</span><span class="p">):</span></span><a href="#l1648"></a>
<span id="l1649">            <span class="k">return</span> <span class="bp">NotImplemented</span></span><a href="#l1649"></a>
<span id="l1650">        <span class="k">else</span><span class="p">:</span></span><a href="#l1650"></a>
<span id="l1651">            <span class="k">return</span> <span class="bp">False</span></span><a href="#l1651"></a>
<span id="l1652"></span><a href="#l1652"></a>
<span id="l1653">    <span class="k">def</span> <span class="nf">__le__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l1653"></a>
<span id="l1654">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">datetime</span><span class="p">):</span></span><a href="#l1654"></a>
<span id="l1655">            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cmp</span><span class="p">(</span><span class="n">other</span><span class="p">)</span> <span class="o">&lt;=</span> <span class="mi">0</span></span><a href="#l1655"></a>
<span id="l1656">        <span class="k">elif</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">date</span><span class="p">):</span></span><a href="#l1656"></a>
<span id="l1657">            <span class="k">return</span> <span class="bp">NotImplemented</span></span><a href="#l1657"></a>
<span id="l1658">        <span class="k">else</span><span class="p">:</span></span><a href="#l1658"></a>
<span id="l1659">            <span class="n">_cmperror</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">)</span></span><a href="#l1659"></a>
<span id="l1660"></span><a href="#l1660"></a>
<span id="l1661">    <span class="k">def</span> <span class="nf">__lt__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l1661"></a>
<span id="l1662">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">datetime</span><span class="p">):</span></span><a href="#l1662"></a>
<span id="l1663">            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cmp</span><span class="p">(</span><span class="n">other</span><span class="p">)</span> <span class="o">&lt;</span> <span class="mi">0</span></span><a href="#l1663"></a>
<span id="l1664">        <span class="k">elif</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">date</span><span class="p">):</span></span><a href="#l1664"></a>
<span id="l1665">            <span class="k">return</span> <span class="bp">NotImplemented</span></span><a href="#l1665"></a>
<span id="l1666">        <span class="k">else</span><span class="p">:</span></span><a href="#l1666"></a>
<span id="l1667">            <span class="n">_cmperror</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">)</span></span><a href="#l1667"></a>
<span id="l1668"></span><a href="#l1668"></a>
<span id="l1669">    <span class="k">def</span> <span class="nf">__ge__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l1669"></a>
<span id="l1670">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">datetime</span><span class="p">):</span></span><a href="#l1670"></a>
<span id="l1671">            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cmp</span><span class="p">(</span><span class="n">other</span><span class="p">)</span> <span class="o">&gt;=</span> <span class="mi">0</span></span><a href="#l1671"></a>
<span id="l1672">        <span class="k">elif</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">date</span><span class="p">):</span></span><a href="#l1672"></a>
<span id="l1673">            <span class="k">return</span> <span class="bp">NotImplemented</span></span><a href="#l1673"></a>
<span id="l1674">        <span class="k">else</span><span class="p">:</span></span><a href="#l1674"></a>
<span id="l1675">            <span class="n">_cmperror</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">)</span></span><a href="#l1675"></a>
<span id="l1676"></span><a href="#l1676"></a>
<span id="l1677">    <span class="k">def</span> <span class="nf">__gt__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l1677"></a>
<span id="l1678">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">datetime</span><span class="p">):</span></span><a href="#l1678"></a>
<span id="l1679">            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cmp</span><span class="p">(</span><span class="n">other</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span></span><a href="#l1679"></a>
<span id="l1680">        <span class="k">elif</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">date</span><span class="p">):</span></span><a href="#l1680"></a>
<span id="l1681">            <span class="k">return</span> <span class="bp">NotImplemented</span></span><a href="#l1681"></a>
<span id="l1682">        <span class="k">else</span><span class="p">:</span></span><a href="#l1682"></a>
<span id="l1683">            <span class="n">_cmperror</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">)</span></span><a href="#l1683"></a>
<span id="l1684"></span><a href="#l1684"></a>
<span id="l1685">    <span class="k">def</span> <span class="nf">_cmp</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">,</span> <span class="n">allow_mixed</span><span class="o">=</span><span class="bp">False</span><span class="p">):</span></span><a href="#l1685"></a>
<span id="l1686">        <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">datetime</span><span class="p">)</span></span><a href="#l1686"></a>
<span id="l1687">        <span class="n">mytz</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tzinfo</span></span><a href="#l1687"></a>
<span id="l1688">        <span class="n">ottz</span> <span class="o">=</span> <span class="n">other</span><span class="o">.</span><span class="n">_tzinfo</span></span><a href="#l1688"></a>
<span id="l1689">        <span class="n">myoff</span> <span class="o">=</span> <span class="n">otoff</span> <span class="o">=</span> <span class="bp">None</span></span><a href="#l1689"></a>
<span id="l1690"></span><a href="#l1690"></a>
<span id="l1691">        <span class="k">if</span> <span class="n">mytz</span> <span class="ow">is</span> <span class="n">ottz</span><span class="p">:</span></span><a href="#l1691"></a>
<span id="l1692">            <span class="n">base_compare</span> <span class="o">=</span> <span class="bp">True</span></span><a href="#l1692"></a>
<span id="l1693">        <span class="k">else</span><span class="p">:</span></span><a href="#l1693"></a>
<span id="l1694">            <span class="n">myoff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">utcoffset</span><span class="p">()</span></span><a href="#l1694"></a>
<span id="l1695">            <span class="n">otoff</span> <span class="o">=</span> <span class="n">other</span><span class="o">.</span><span class="n">utcoffset</span><span class="p">()</span></span><a href="#l1695"></a>
<span id="l1696">            <span class="n">base_compare</span> <span class="o">=</span> <span class="n">myoff</span> <span class="o">==</span> <span class="n">otoff</span></span><a href="#l1696"></a>
<span id="l1697"></span><a href="#l1697"></a>
<span id="l1698">        <span class="k">if</span> <span class="n">base_compare</span><span class="p">:</span></span><a href="#l1698"></a>
<span id="l1699">            <span class="k">return</span> <span class="n">_cmp</span><span class="p">((</span><span class="bp">self</span><span class="o">.</span><span class="n">_year</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_month</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_day</span><span class="p">,</span></span><a href="#l1699"></a>
<span id="l1700">                         <span class="bp">self</span><span class="o">.</span><span class="n">_hour</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_minute</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_second</span><span class="p">,</span></span><a href="#l1700"></a>
<span id="l1701">                         <span class="bp">self</span><span class="o">.</span><span class="n">_microsecond</span><span class="p">),</span></span><a href="#l1701"></a>
<span id="l1702">                        <span class="p">(</span><span class="n">other</span><span class="o">.</span><span class="n">_year</span><span class="p">,</span> <span class="n">other</span><span class="o">.</span><span class="n">_month</span><span class="p">,</span> <span class="n">other</span><span class="o">.</span><span class="n">_day</span><span class="p">,</span></span><a href="#l1702"></a>
<span id="l1703">                         <span class="n">other</span><span class="o">.</span><span class="n">_hour</span><span class="p">,</span> <span class="n">other</span><span class="o">.</span><span class="n">_minute</span><span class="p">,</span> <span class="n">other</span><span class="o">.</span><span class="n">_second</span><span class="p">,</span></span><a href="#l1703"></a>
<span id="l1704">                         <span class="n">other</span><span class="o">.</span><span class="n">_microsecond</span><span class="p">))</span></span><a href="#l1704"></a>
<span id="l1705">        <span class="k">if</span> <span class="n">myoff</span> <span class="ow">is</span> <span class="bp">None</span> <span class="ow">or</span> <span class="n">otoff</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1705"></a>
<span id="l1706">            <span class="k">if</span> <span class="n">allow_mixed</span><span class="p">:</span></span><a href="#l1706"></a>
<span id="l1707">                <span class="k">return</span> <span class="mi">2</span> <span class="c"># arbitrary non-zero value</span></span><a href="#l1707"></a>
<span id="l1708">            <span class="k">else</span><span class="p">:</span></span><a href="#l1708"></a>
<span id="l1709">                <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="s">&quot;cannot compare naive and aware datetimes&quot;</span><span class="p">)</span></span><a href="#l1709"></a>
<span id="l1710">        <span class="c"># XXX What follows could be done more efficiently...</span></span><a href="#l1710"></a>
<span id="l1711">        <span class="n">diff</span> <span class="o">=</span> <span class="bp">self</span> <span class="o">-</span> <span class="n">other</span>     <span class="c"># this will take offsets into account</span></span><a href="#l1711"></a>
<span id="l1712">        <span class="k">if</span> <span class="n">diff</span><span class="o">.</span><span class="n">days</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span></span><a href="#l1712"></a>
<span id="l1713">            <span class="k">return</span> <span class="o">-</span><span class="mi">1</span></span><a href="#l1713"></a>
<span id="l1714">        <span class="k">return</span> <span class="n">diff</span> <span class="ow">and</span> <span class="mi">1</span> <span class="ow">or</span> <span class="mi">0</span></span><a href="#l1714"></a>
<span id="l1715"></span><a href="#l1715"></a>
<span id="l1716">    <span class="k">def</span> <span class="nf">__add__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l1716"></a>
<span id="l1717">        <span class="s">&quot;Add a datetime and a timedelta.&quot;</span></span><a href="#l1717"></a>
<span id="l1718">        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">timedelta</span><span class="p">):</span></span><a href="#l1718"></a>
<span id="l1719">            <span class="k">return</span> <span class="bp">NotImplemented</span></span><a href="#l1719"></a>
<span id="l1720">        <span class="n">delta</span> <span class="o">=</span> <span class="n">timedelta</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">toordinal</span><span class="p">(),</span></span><a href="#l1720"></a>
<span id="l1721">                          <span class="n">hours</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_hour</span><span class="p">,</span></span><a href="#l1721"></a>
<span id="l1722">                          <span class="n">minutes</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_minute</span><span class="p">,</span></span><a href="#l1722"></a>
<span id="l1723">                          <span class="n">seconds</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_second</span><span class="p">,</span></span><a href="#l1723"></a>
<span id="l1724">                          <span class="n">microseconds</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_microsecond</span><span class="p">)</span></span><a href="#l1724"></a>
<span id="l1725">        <span class="n">delta</span> <span class="o">+=</span> <span class="n">other</span></span><a href="#l1725"></a>
<span id="l1726">        <span class="n">hour</span><span class="p">,</span> <span class="n">rem</span> <span class="o">=</span> <span class="nb">divmod</span><span class="p">(</span><span class="n">delta</span><span class="o">.</span><span class="n">seconds</span><span class="p">,</span> <span class="mi">3600</span><span class="p">)</span></span><a href="#l1726"></a>
<span id="l1727">        <span class="n">minute</span><span class="p">,</span> <span class="n">second</span> <span class="o">=</span> <span class="nb">divmod</span><span class="p">(</span><span class="n">rem</span><span class="p">,</span> <span class="mi">60</span><span class="p">)</span></span><a href="#l1727"></a>
<span id="l1728">        <span class="k">if</span> <span class="mi">0</span> <span class="o">&lt;</span> <span class="n">delta</span><span class="o">.</span><span class="n">days</span> <span class="o">&lt;=</span> <span class="n">_MAXORDINAL</span><span class="p">:</span></span><a href="#l1728"></a>
<span id="l1729">            <span class="k">return</span> <span class="n">datetime</span><span class="o">.</span><span class="n">combine</span><span class="p">(</span><span class="n">date</span><span class="o">.</span><span class="n">fromordinal</span><span class="p">(</span><span class="n">delta</span><span class="o">.</span><span class="n">days</span><span class="p">),</span></span><a href="#l1729"></a>
<span id="l1730">                                    <span class="n">time</span><span class="p">(</span><span class="n">hour</span><span class="p">,</span> <span class="n">minute</span><span class="p">,</span> <span class="n">second</span><span class="p">,</span></span><a href="#l1730"></a>
<span id="l1731">                                         <span class="n">delta</span><span class="o">.</span><span class="n">microseconds</span><span class="p">,</span></span><a href="#l1731"></a>
<span id="l1732">                                         <span class="n">tzinfo</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_tzinfo</span><span class="p">))</span></span><a href="#l1732"></a>
<span id="l1733">        <span class="k">raise</span> <span class="ne">OverflowError</span><span class="p">(</span><span class="s">&quot;result out of range&quot;</span><span class="p">)</span></span><a href="#l1733"></a>
<span id="l1734"></span><a href="#l1734"></a>
<span id="l1735">    <span class="n">__radd__</span> <span class="o">=</span> <span class="n">__add__</span></span><a href="#l1735"></a>
<span id="l1736"></span><a href="#l1736"></a>
<span id="l1737">    <span class="k">def</span> <span class="nf">__sub__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l1737"></a>
<span id="l1738">        <span class="s">&quot;Subtract two datetimes, or a datetime and a timedelta.&quot;</span></span><a href="#l1738"></a>
<span id="l1739">        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">datetime</span><span class="p">):</span></span><a href="#l1739"></a>
<span id="l1740">            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">other</span><span class="p">,</span> <span class="n">timedelta</span><span class="p">):</span></span><a href="#l1740"></a>
<span id="l1741">                <span class="k">return</span> <span class="bp">self</span> <span class="o">+</span> <span class="o">-</span><span class="n">other</span></span><a href="#l1741"></a>
<span id="l1742">            <span class="k">return</span> <span class="bp">NotImplemented</span></span><a href="#l1742"></a>
<span id="l1743"></span><a href="#l1743"></a>
<span id="l1744">        <span class="n">days1</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">toordinal</span><span class="p">()</span></span><a href="#l1744"></a>
<span id="l1745">        <span class="n">days2</span> <span class="o">=</span> <span class="n">other</span><span class="o">.</span><span class="n">toordinal</span><span class="p">()</span></span><a href="#l1745"></a>
<span id="l1746">        <span class="n">secs1</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_second</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">_minute</span> <span class="o">*</span> <span class="mi">60</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">_hour</span> <span class="o">*</span> <span class="mi">3600</span></span><a href="#l1746"></a>
<span id="l1747">        <span class="n">secs2</span> <span class="o">=</span> <span class="n">other</span><span class="o">.</span><span class="n">_second</span> <span class="o">+</span> <span class="n">other</span><span class="o">.</span><span class="n">_minute</span> <span class="o">*</span> <span class="mi">60</span> <span class="o">+</span> <span class="n">other</span><span class="o">.</span><span class="n">_hour</span> <span class="o">*</span> <span class="mi">3600</span></span><a href="#l1747"></a>
<span id="l1748">        <span class="n">base</span> <span class="o">=</span> <span class="n">timedelta</span><span class="p">(</span><span class="n">days1</span> <span class="o">-</span> <span class="n">days2</span><span class="p">,</span></span><a href="#l1748"></a>
<span id="l1749">                         <span class="n">secs1</span> <span class="o">-</span> <span class="n">secs2</span><span class="p">,</span></span><a href="#l1749"></a>
<span id="l1750">                         <span class="bp">self</span><span class="o">.</span><span class="n">_microsecond</span> <span class="o">-</span> <span class="n">other</span><span class="o">.</span><span class="n">_microsecond</span><span class="p">)</span></span><a href="#l1750"></a>
<span id="l1751">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tzinfo</span> <span class="ow">is</span> <span class="n">other</span><span class="o">.</span><span class="n">_tzinfo</span><span class="p">:</span></span><a href="#l1751"></a>
<span id="l1752">            <span class="k">return</span> <span class="n">base</span></span><a href="#l1752"></a>
<span id="l1753">        <span class="n">myoff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">utcoffset</span><span class="p">()</span></span><a href="#l1753"></a>
<span id="l1754">        <span class="n">otoff</span> <span class="o">=</span> <span class="n">other</span><span class="o">.</span><span class="n">utcoffset</span><span class="p">()</span></span><a href="#l1754"></a>
<span id="l1755">        <span class="k">if</span> <span class="n">myoff</span> <span class="o">==</span> <span class="n">otoff</span><span class="p">:</span></span><a href="#l1755"></a>
<span id="l1756">            <span class="k">return</span> <span class="n">base</span></span><a href="#l1756"></a>
<span id="l1757">        <span class="k">if</span> <span class="n">myoff</span> <span class="ow">is</span> <span class="bp">None</span> <span class="ow">or</span> <span class="n">otoff</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1757"></a>
<span id="l1758">            <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="s">&quot;cannot mix naive and timezone-aware time&quot;</span><span class="p">)</span></span><a href="#l1758"></a>
<span id="l1759">        <span class="k">return</span> <span class="n">base</span> <span class="o">+</span> <span class="n">otoff</span> <span class="o">-</span> <span class="n">myoff</span></span><a href="#l1759"></a>
<span id="l1760"></span><a href="#l1760"></a>
<span id="l1761">    <span class="k">def</span> <span class="nf">__hash__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1761"></a>
<span id="l1762">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_hashcode</span> <span class="o">==</span> <span class="o">-</span><span class="mi">1</span><span class="p">:</span></span><a href="#l1762"></a>
<span id="l1763">            <span class="n">tzoff</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">utcoffset</span><span class="p">()</span></span><a href="#l1763"></a>
<span id="l1764">            <span class="k">if</span> <span class="n">tzoff</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1764"></a>
<span id="l1765">                <span class="bp">self</span><span class="o">.</span><span class="n">_hashcode</span> <span class="o">=</span> <span class="nb">hash</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_getstate</span><span class="p">()[</span><span class="mi">0</span><span class="p">])</span></span><a href="#l1765"></a>
<span id="l1766">            <span class="k">else</span><span class="p">:</span></span><a href="#l1766"></a>
<span id="l1767">                <span class="n">days</span> <span class="o">=</span> <span class="n">_ymd2ord</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">year</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">month</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">day</span><span class="p">)</span></span><a href="#l1767"></a>
<span id="l1768">                <span class="n">seconds</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">hour</span> <span class="o">*</span> <span class="mi">3600</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">minute</span> <span class="o">*</span> <span class="mi">60</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">second</span></span><a href="#l1768"></a>
<span id="l1769">                <span class="bp">self</span><span class="o">.</span><span class="n">_hashcode</span> <span class="o">=</span> <span class="nb">hash</span><span class="p">(</span><span class="n">timedelta</span><span class="p">(</span><span class="n">days</span><span class="p">,</span> <span class="n">seconds</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">microsecond</span><span class="p">)</span> <span class="o">-</span> <span class="n">tzoff</span><span class="p">)</span></span><a href="#l1769"></a>
<span id="l1770">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_hashcode</span></span><a href="#l1770"></a>
<span id="l1771"></span><a href="#l1771"></a>
<span id="l1772">    <span class="c"># Pickle support.</span></span><a href="#l1772"></a>
<span id="l1773"></span><a href="#l1773"></a>
<span id="l1774">    <span class="k">def</span> <span class="nf">_getstate</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1774"></a>
<span id="l1775">        <span class="n">yhi</span><span class="p">,</span> <span class="n">ylo</span> <span class="o">=</span> <span class="nb">divmod</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_year</span><span class="p">,</span> <span class="mi">256</span><span class="p">)</span></span><a href="#l1775"></a>
<span id="l1776">        <span class="n">us2</span><span class="p">,</span> <span class="n">us3</span> <span class="o">=</span> <span class="nb">divmod</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_microsecond</span><span class="p">,</span> <span class="mi">256</span><span class="p">)</span></span><a href="#l1776"></a>
<span id="l1777">        <span class="n">us1</span><span class="p">,</span> <span class="n">us2</span> <span class="o">=</span> <span class="nb">divmod</span><span class="p">(</span><span class="n">us2</span><span class="p">,</span> <span class="mi">256</span><span class="p">)</span></span><a href="#l1777"></a>
<span id="l1778">        <span class="n">basestate</span> <span class="o">=</span> <span class="nb">bytes</span><span class="p">([</span><span class="n">yhi</span><span class="p">,</span> <span class="n">ylo</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_month</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_day</span><span class="p">,</span></span><a href="#l1778"></a>
<span id="l1779">                           <span class="bp">self</span><span class="o">.</span><span class="n">_hour</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_minute</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_second</span><span class="p">,</span></span><a href="#l1779"></a>
<span id="l1780">                           <span class="n">us1</span><span class="p">,</span> <span class="n">us2</span><span class="p">,</span> <span class="n">us3</span><span class="p">])</span></span><a href="#l1780"></a>
<span id="l1781">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tzinfo</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1781"></a>
<span id="l1782">            <span class="k">return</span> <span class="p">(</span><span class="n">basestate</span><span class="p">,)</span></span><a href="#l1782"></a>
<span id="l1783">        <span class="k">else</span><span class="p">:</span></span><a href="#l1783"></a>
<span id="l1784">            <span class="k">return</span> <span class="p">(</span><span class="n">basestate</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_tzinfo</span><span class="p">)</span></span><a href="#l1784"></a>
<span id="l1785"></span><a href="#l1785"></a>
<span id="l1786">    <span class="k">def</span> <span class="nf">__setstate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">string</span><span class="p">,</span> <span class="n">tzinfo</span><span class="p">):</span></span><a href="#l1786"></a>
<span id="l1787">        <span class="k">if</span> <span class="n">tzinfo</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span> <span class="ow">and</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">tzinfo</span><span class="p">,</span> <span class="n">_tzinfo_class</span><span class="p">):</span></span><a href="#l1787"></a>
<span id="l1788">            <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="s">&quot;bad tzinfo state arg&quot;</span><span class="p">)</span></span><a href="#l1788"></a>
<span id="l1789">        <span class="p">(</span><span class="n">yhi</span><span class="p">,</span> <span class="n">ylo</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_month</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_day</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_hour</span><span class="p">,</span></span><a href="#l1789"></a>
<span id="l1790">         <span class="bp">self</span><span class="o">.</span><span class="n">_minute</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_second</span><span class="p">,</span> <span class="n">us1</span><span class="p">,</span> <span class="n">us2</span><span class="p">,</span> <span class="n">us3</span><span class="p">)</span> <span class="o">=</span> <span class="n">string</span></span><a href="#l1790"></a>
<span id="l1791">        <span class="bp">self</span><span class="o">.</span><span class="n">_year</span> <span class="o">=</span> <span class="n">yhi</span> <span class="o">*</span> <span class="mi">256</span> <span class="o">+</span> <span class="n">ylo</span></span><a href="#l1791"></a>
<span id="l1792">        <span class="bp">self</span><span class="o">.</span><span class="n">_microsecond</span> <span class="o">=</span> <span class="p">(((</span><span class="n">us1</span> <span class="o">&lt;&lt;</span> <span class="mi">8</span><span class="p">)</span> <span class="o">|</span> <span class="n">us2</span><span class="p">)</span> <span class="o">&lt;&lt;</span> <span class="mi">8</span><span class="p">)</span> <span class="o">|</span> <span class="n">us3</span></span><a href="#l1792"></a>
<span id="l1793">        <span class="bp">self</span><span class="o">.</span><span class="n">_tzinfo</span> <span class="o">=</span> <span class="n">tzinfo</span></span><a href="#l1793"></a>
<span id="l1794"></span><a href="#l1794"></a>
<span id="l1795">    <span class="k">def</span> <span class="nf">__reduce__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1795"></a>
<span id="l1796">        <span class="k">return</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__class__</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_getstate</span><span class="p">())</span></span><a href="#l1796"></a>
<span id="l1797"></span><a href="#l1797"></a>
<span id="l1798"></span><a href="#l1798"></a>
<span id="l1799"><span class="n">datetime</span><span class="o">.</span><span class="n">min</span> <span class="o">=</span> <span class="n">datetime</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span></span><a href="#l1799"></a>
<span id="l1800"><span class="n">datetime</span><span class="o">.</span><span class="n">max</span> <span class="o">=</span> <span class="n">datetime</span><span class="p">(</span><span class="mi">9999</span><span class="p">,</span> <span class="mi">12</span><span class="p">,</span> <span class="mi">31</span><span class="p">,</span> <span class="mi">23</span><span class="p">,</span> <span class="mi">59</span><span class="p">,</span> <span class="mi">59</span><span class="p">,</span> <span class="mi">999999</span><span class="p">)</span></span><a href="#l1800"></a>
<span id="l1801"><span class="n">datetime</span><span class="o">.</span><span class="n">resolution</span> <span class="o">=</span> <span class="n">timedelta</span><span class="p">(</span><span class="n">microseconds</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span></span><a href="#l1801"></a>
<span id="l1802"></span><a href="#l1802"></a>
<span id="l1803"></span><a href="#l1803"></a>
<span id="l1804"><span class="k">def</span> <span class="nf">_isoweek1monday</span><span class="p">(</span><span class="n">year</span><span class="p">):</span></span><a href="#l1804"></a>
<span id="l1805">    <span class="c"># Helper to calculate the day number of the Monday starting week 1</span></span><a href="#l1805"></a>
<span id="l1806">    <span class="c"># XXX This could be done more efficiently</span></span><a href="#l1806"></a>
<span id="l1807">    <span class="n">THURSDAY</span> <span class="o">=</span> <span class="mi">3</span></span><a href="#l1807"></a>
<span id="l1808">    <span class="n">firstday</span> <span class="o">=</span> <span class="n">_ymd2ord</span><span class="p">(</span><span class="n">year</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span></span><a href="#l1808"></a>
<span id="l1809">    <span class="n">firstweekday</span> <span class="o">=</span> <span class="p">(</span><span class="n">firstday</span> <span class="o">+</span> <span class="mi">6</span><span class="p">)</span> <span class="o">%</span> <span class="mi">7</span>  <span class="c"># See weekday() above</span></span><a href="#l1809"></a>
<span id="l1810">    <span class="n">week1monday</span> <span class="o">=</span> <span class="n">firstday</span> <span class="o">-</span> <span class="n">firstweekday</span></span><a href="#l1810"></a>
<span id="l1811">    <span class="k">if</span> <span class="n">firstweekday</span> <span class="o">&gt;</span> <span class="n">THURSDAY</span><span class="p">:</span></span><a href="#l1811"></a>
<span id="l1812">        <span class="n">week1monday</span> <span class="o">+=</span> <span class="mi">7</span></span><a href="#l1812"></a>
<span id="l1813">    <span class="k">return</span> <span class="n">week1monday</span></span><a href="#l1813"></a>
<span id="l1814"></span><a href="#l1814"></a>
<span id="l1815"><span class="k">class</span> <span class="nc">timezone</span><span class="p">(</span><span class="n">tzinfo</span><span class="p">):</span></span><a href="#l1815"></a>
<span id="l1816">    <span class="n">__slots__</span> <span class="o">=</span> <span class="s">&#39;_offset&#39;</span><span class="p">,</span> <span class="s">&#39;_name&#39;</span></span><a href="#l1816"></a>
<span id="l1817"></span><a href="#l1817"></a>
<span id="l1818">    <span class="c"># Sentinel value to disallow None</span></span><a href="#l1818"></a>
<span id="l1819">    <span class="n">_Omitted</span> <span class="o">=</span> <span class="nb">object</span><span class="p">()</span></span><a href="#l1819"></a>
<span id="l1820">    <span class="k">def</span> <span class="nf">__new__</span><span class="p">(</span><span class="n">cls</span><span class="p">,</span> <span class="n">offset</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">_Omitted</span><span class="p">):</span></span><a href="#l1820"></a>
<span id="l1821">        <span class="k">if</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">offset</span><span class="p">,</span> <span class="n">timedelta</span><span class="p">):</span></span><a href="#l1821"></a>
<span id="l1822">            <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="s">&quot;offset must be a timedelta&quot;</span><span class="p">)</span></span><a href="#l1822"></a>
<span id="l1823">        <span class="k">if</span> <span class="n">name</span> <span class="ow">is</span> <span class="n">cls</span><span class="o">.</span><span class="n">_Omitted</span><span class="p">:</span></span><a href="#l1823"></a>
<span id="l1824">            <span class="k">if</span> <span class="ow">not</span> <span class="n">offset</span><span class="p">:</span></span><a href="#l1824"></a>
<span id="l1825">                <span class="k">return</span> <span class="n">cls</span><span class="o">.</span><span class="n">utc</span></span><a href="#l1825"></a>
<span id="l1826">            <span class="n">name</span> <span class="o">=</span> <span class="bp">None</span></span><a href="#l1826"></a>
<span id="l1827">        <span class="k">elif</span> <span class="ow">not</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="nb">str</span><span class="p">):</span></span><a href="#l1827"></a>
<span id="l1828">            <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="s">&quot;name must be a string&quot;</span><span class="p">)</span></span><a href="#l1828"></a>
<span id="l1829">        <span class="k">if</span> <span class="ow">not</span> <span class="n">cls</span><span class="o">.</span><span class="n">_minoffset</span> <span class="o">&lt;=</span> <span class="n">offset</span> <span class="o">&lt;=</span> <span class="n">cls</span><span class="o">.</span><span class="n">_maxoffset</span><span class="p">:</span></span><a href="#l1829"></a>
<span id="l1830">            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&quot;offset must be a timedelta &quot;</span></span><a href="#l1830"></a>
<span id="l1831">                             <span class="s">&quot;strictly between -timedelta(hours=24) and &quot;</span></span><a href="#l1831"></a>
<span id="l1832">                             <span class="s">&quot;timedelta(hours=24).&quot;</span><span class="p">)</span></span><a href="#l1832"></a>
<span id="l1833">        <span class="k">if</span> <span class="p">(</span><span class="n">offset</span><span class="o">.</span><span class="n">microseconds</span> <span class="o">!=</span> <span class="mi">0</span> <span class="ow">or</span> <span class="n">offset</span><span class="o">.</span><span class="n">seconds</span> <span class="o">%</span> <span class="mi">60</span> <span class="o">!=</span> <span class="mi">0</span><span class="p">):</span></span><a href="#l1833"></a>
<span id="l1834">            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&quot;offset must be a timedelta &quot;</span></span><a href="#l1834"></a>
<span id="l1835">                             <span class="s">&quot;representing a whole number of minutes&quot;</span><span class="p">)</span></span><a href="#l1835"></a>
<span id="l1836">        <span class="k">return</span> <span class="n">cls</span><span class="o">.</span><span class="n">_create</span><span class="p">(</span><span class="n">offset</span><span class="p">,</span> <span class="n">name</span><span class="p">)</span></span><a href="#l1836"></a>
<span id="l1837"></span><a href="#l1837"></a>
<span id="l1838">    <span class="nd">@classmethod</span></span><a href="#l1838"></a>
<span id="l1839">    <span class="k">def</span> <span class="nf">_create</span><span class="p">(</span><span class="n">cls</span><span class="p">,</span> <span class="n">offset</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l1839"></a>
<span id="l1840">        <span class="bp">self</span> <span class="o">=</span> <span class="n">tzinfo</span><span class="o">.</span><span class="n">__new__</span><span class="p">(</span><span class="n">cls</span><span class="p">)</span></span><a href="#l1840"></a>
<span id="l1841">        <span class="bp">self</span><span class="o">.</span><span class="n">_offset</span> <span class="o">=</span> <span class="n">offset</span></span><a href="#l1841"></a>
<span id="l1842">        <span class="bp">self</span><span class="o">.</span><span class="n">_name</span> <span class="o">=</span> <span class="n">name</span></span><a href="#l1842"></a>
<span id="l1843">        <span class="k">return</span> <span class="bp">self</span></span><a href="#l1843"></a>
<span id="l1844"></span><a href="#l1844"></a>
<span id="l1845">    <span class="k">def</span> <span class="nf">__getinitargs__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1845"></a>
<span id="l1846">        <span class="sd">&quot;&quot;&quot;pickle support&quot;&quot;&quot;</span></span><a href="#l1846"></a>
<span id="l1847">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_name</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1847"></a>
<span id="l1848">            <span class="k">return</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_offset</span><span class="p">,)</span></span><a href="#l1848"></a>
<span id="l1849">        <span class="k">return</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_offset</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_name</span><span class="p">)</span></span><a href="#l1849"></a>
<span id="l1850"></span><a href="#l1850"></a>
<span id="l1851">    <span class="k">def</span> <span class="nf">__eq__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span></span><a href="#l1851"></a>
<span id="l1852">        <span class="k">if</span> <span class="nb">type</span><span class="p">(</span><span class="n">other</span><span class="p">)</span> <span class="o">!=</span> <span class="n">timezone</span><span class="p">:</span></span><a href="#l1852"></a>
<span id="l1853">            <span class="k">return</span> <span class="bp">False</span></span><a href="#l1853"></a>
<span id="l1854">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_offset</span> <span class="o">==</span> <span class="n">other</span><span class="o">.</span><span class="n">_offset</span></span><a href="#l1854"></a>
<span id="l1855"></span><a href="#l1855"></a>
<span id="l1856">    <span class="k">def</span> <span class="nf">__hash__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1856"></a>
<span id="l1857">        <span class="k">return</span> <span class="nb">hash</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_offset</span><span class="p">)</span></span><a href="#l1857"></a>
<span id="l1858"></span><a href="#l1858"></a>
<span id="l1859">    <span class="k">def</span> <span class="nf">__repr__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1859"></a>
<span id="l1860">        <span class="sd">&quot;&quot;&quot;Convert to formal string, for repr().</span></span><a href="#l1860"></a>
<span id="l1861"></span><a href="#l1861"></a>
<span id="l1862"><span class="sd">        &gt;&gt;&gt; tz = timezone.utc</span></span><a href="#l1862"></a>
<span id="l1863"><span class="sd">        &gt;&gt;&gt; repr(tz)</span></span><a href="#l1863"></a>
<span id="l1864"><span class="sd">        &#39;datetime.timezone.utc&#39;</span></span><a href="#l1864"></a>
<span id="l1865"><span class="sd">        &gt;&gt;&gt; tz = timezone(timedelta(hours=-5), &#39;EST&#39;)</span></span><a href="#l1865"></a>
<span id="l1866"><span class="sd">        &gt;&gt;&gt; repr(tz)</span></span><a href="#l1866"></a>
<span id="l1867"><span class="sd">        &quot;datetime.timezone(datetime.timedelta(-1, 68400), &#39;EST&#39;)&quot;</span></span><a href="#l1867"></a>
<span id="l1868"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l1868"></a>
<span id="l1869">        <span class="k">if</span> <span class="bp">self</span> <span class="ow">is</span> <span class="bp">self</span><span class="o">.</span><span class="n">utc</span><span class="p">:</span></span><a href="#l1869"></a>
<span id="l1870">            <span class="k">return</span> <span class="s">&#39;datetime.timezone.utc&#39;</span></span><a href="#l1870"></a>
<span id="l1871">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_name</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1871"></a>
<span id="l1872">            <span class="k">return</span> <span class="s">&quot;</span><span class="si">%s</span><span class="s">.</span><span class="si">%s</span><span class="s">(</span><span class="si">%r</span><span class="s">)&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__class__</span><span class="o">.</span><span class="n">__module__</span><span class="p">,</span></span><a href="#l1872"></a>
<span id="l1873">                                  <span class="bp">self</span><span class="o">.</span><span class="n">__class__</span><span class="o">.</span><span class="n">__qualname__</span><span class="p">,</span></span><a href="#l1873"></a>
<span id="l1874">                                  <span class="bp">self</span><span class="o">.</span><span class="n">_offset</span><span class="p">)</span></span><a href="#l1874"></a>
<span id="l1875">        <span class="k">return</span> <span class="s">&quot;</span><span class="si">%s</span><span class="s">.</span><span class="si">%s</span><span class="s">(</span><span class="si">%r</span><span class="s">, </span><span class="si">%r</span><span class="s">)&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__class__</span><span class="o">.</span><span class="n">__module__</span><span class="p">,</span></span><a href="#l1875"></a>
<span id="l1876">                                  <span class="bp">self</span><span class="o">.</span><span class="n">__class__</span><span class="o">.</span><span class="n">__qualname__</span><span class="p">,</span></span><a href="#l1876"></a>
<span id="l1877">                                  <span class="bp">self</span><span class="o">.</span><span class="n">_offset</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_name</span><span class="p">)</span></span><a href="#l1877"></a>
<span id="l1878"></span><a href="#l1878"></a>
<span id="l1879">    <span class="k">def</span> <span class="nf">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l1879"></a>
<span id="l1880">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">tzname</span><span class="p">(</span><span class="bp">None</span><span class="p">)</span></span><a href="#l1880"></a>
<span id="l1881"></span><a href="#l1881"></a>
<span id="l1882">    <span class="k">def</span> <span class="nf">utcoffset</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">dt</span><span class="p">):</span></span><a href="#l1882"></a>
<span id="l1883">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">dt</span><span class="p">,</span> <span class="n">datetime</span><span class="p">)</span> <span class="ow">or</span> <span class="n">dt</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1883"></a>
<span id="l1884">            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_offset</span></span><a href="#l1884"></a>
<span id="l1885">        <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="s">&quot;utcoffset() argument must be a datetime instance&quot;</span></span><a href="#l1885"></a>
<span id="l1886">                        <span class="s">&quot; or None&quot;</span><span class="p">)</span></span><a href="#l1886"></a>
<span id="l1887"></span><a href="#l1887"></a>
<span id="l1888">    <span class="k">def</span> <span class="nf">tzname</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">dt</span><span class="p">):</span></span><a href="#l1888"></a>
<span id="l1889">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">dt</span><span class="p">,</span> <span class="n">datetime</span><span class="p">)</span> <span class="ow">or</span> <span class="n">dt</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1889"></a>
<span id="l1890">            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_name</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1890"></a>
<span id="l1891">                <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_name_from_offset</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_offset</span><span class="p">)</span></span><a href="#l1891"></a>
<span id="l1892">            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_name</span></span><a href="#l1892"></a>
<span id="l1893">        <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="s">&quot;tzname() argument must be a datetime instance&quot;</span></span><a href="#l1893"></a>
<span id="l1894">                        <span class="s">&quot; or None&quot;</span><span class="p">)</span></span><a href="#l1894"></a>
<span id="l1895"></span><a href="#l1895"></a>
<span id="l1896">    <span class="k">def</span> <span class="nf">dst</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">dt</span><span class="p">):</span></span><a href="#l1896"></a>
<span id="l1897">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">dt</span><span class="p">,</span> <span class="n">datetime</span><span class="p">)</span> <span class="ow">or</span> <span class="n">dt</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l1897"></a>
<span id="l1898">            <span class="k">return</span> <span class="bp">None</span></span><a href="#l1898"></a>
<span id="l1899">        <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="s">&quot;dst() argument must be a datetime instance&quot;</span></span><a href="#l1899"></a>
<span id="l1900">                        <span class="s">&quot; or None&quot;</span><span class="p">)</span></span><a href="#l1900"></a>
<span id="l1901"></span><a href="#l1901"></a>
<span id="l1902">    <span class="k">def</span> <span class="nf">fromutc</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">dt</span><span class="p">):</span></span><a href="#l1902"></a>
<span id="l1903">        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">dt</span><span class="p">,</span> <span class="n">datetime</span><span class="p">):</span></span><a href="#l1903"></a>
<span id="l1904">            <span class="k">if</span> <span class="n">dt</span><span class="o">.</span><span class="n">tzinfo</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">self</span><span class="p">:</span></span><a href="#l1904"></a>
<span id="l1905">                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&quot;fromutc: dt.tzinfo &quot;</span></span><a href="#l1905"></a>
<span id="l1906">                                 <span class="s">&quot;is not self&quot;</span><span class="p">)</span></span><a href="#l1906"></a>
<span id="l1907">            <span class="k">return</span> <span class="n">dt</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">_offset</span></span><a href="#l1907"></a>
<span id="l1908">        <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">(</span><span class="s">&quot;fromutc() argument must be a datetime instance&quot;</span></span><a href="#l1908"></a>
<span id="l1909">                        <span class="s">&quot; or None&quot;</span><span class="p">)</span></span><a href="#l1909"></a>
<span id="l1910"></span><a href="#l1910"></a>
<span id="l1911">    <span class="n">_maxoffset</span> <span class="o">=</span> <span class="n">timedelta</span><span class="p">(</span><span class="n">hours</span><span class="o">=</span><span class="mi">23</span><span class="p">,</span> <span class="n">minutes</span><span class="o">=</span><span class="mi">59</span><span class="p">)</span></span><a href="#l1911"></a>
<span id="l1912">    <span class="n">_minoffset</span> <span class="o">=</span> <span class="o">-</span><span class="n">_maxoffset</span></span><a href="#l1912"></a>
<span id="l1913"></span><a href="#l1913"></a>
<span id="l1914">    <span class="nd">@staticmethod</span></span><a href="#l1914"></a>
<span id="l1915">    <span class="k">def</span> <span class="nf">_name_from_offset</span><span class="p">(</span><span class="n">delta</span><span class="p">):</span></span><a href="#l1915"></a>
<span id="l1916">        <span class="k">if</span> <span class="n">delta</span> <span class="o">&lt;</span> <span class="n">timedelta</span><span class="p">(</span><span class="mi">0</span><span class="p">):</span></span><a href="#l1916"></a>
<span id="l1917">            <span class="n">sign</span> <span class="o">=</span> <span class="s">&#39;-&#39;</span></span><a href="#l1917"></a>
<span id="l1918">            <span class="n">delta</span> <span class="o">=</span> <span class="o">-</span><span class="n">delta</span></span><a href="#l1918"></a>
<span id="l1919">        <span class="k">else</span><span class="p">:</span></span><a href="#l1919"></a>
<span id="l1920">            <span class="n">sign</span> <span class="o">=</span> <span class="s">&#39;+&#39;</span></span><a href="#l1920"></a>
<span id="l1921">        <span class="n">hours</span><span class="p">,</span> <span class="n">rest</span> <span class="o">=</span> <span class="nb">divmod</span><span class="p">(</span><span class="n">delta</span><span class="p">,</span> <span class="n">timedelta</span><span class="p">(</span><span class="n">hours</span><span class="o">=</span><span class="mi">1</span><span class="p">))</span></span><a href="#l1921"></a>
<span id="l1922">        <span class="n">minutes</span> <span class="o">=</span> <span class="n">rest</span> <span class="o">//</span> <span class="n">timedelta</span><span class="p">(</span><span class="n">minutes</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span></span><a href="#l1922"></a>
<span id="l1923">        <span class="k">return</span> <span class="s">&#39;UTC{}{:02d}:{:02d}&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">sign</span><span class="p">,</span> <span class="n">hours</span><span class="p">,</span> <span class="n">minutes</span><span class="p">)</span></span><a href="#l1923"></a>
<span id="l1924"></span><a href="#l1924"></a>
<span id="l1925"><span class="n">timezone</span><span class="o">.</span><span class="n">utc</span> <span class="o">=</span> <span class="n">timezone</span><span class="o">.</span><span class="n">_create</span><span class="p">(</span><span class="n">timedelta</span><span class="p">(</span><span class="mi">0</span><span class="p">))</span></span><a href="#l1925"></a>
<span id="l1926"><span class="n">timezone</span><span class="o">.</span><span class="n">min</span> <span class="o">=</span> <span class="n">timezone</span><span class="o">.</span><span class="n">_create</span><span class="p">(</span><span class="n">timezone</span><span class="o">.</span><span class="n">_minoffset</span><span class="p">)</span></span><a href="#l1926"></a>
<span id="l1927"><span class="n">timezone</span><span class="o">.</span><span class="n">max</span> <span class="o">=</span> <span class="n">timezone</span><span class="o">.</span><span class="n">_create</span><span class="p">(</span><span class="n">timezone</span><span class="o">.</span><span class="n">_maxoffset</span><span class="p">)</span></span><a href="#l1927"></a>
<span id="l1928"><span class="n">_EPOCH</span> <span class="o">=</span> <span class="n">datetime</span><span class="p">(</span><span class="mi">1970</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="n">tzinfo</span><span class="o">=</span><span class="n">timezone</span><span class="o">.</span><span class="n">utc</span><span class="p">)</span></span><a href="#l1928"></a>
<span id="l1929"></span><a href="#l1929"></a>
<span id="l1930"><span class="c"># Some time zone algebra.  For a datetime x, let</span></span><a href="#l1930"></a>
<span id="l1931"><span class="c">#     x.n = x stripped of its timezone -- its naive time.</span></span><a href="#l1931"></a>
<span id="l1932"><span class="c">#     x.o = x.utcoffset(), and assuming that doesn&#39;t raise an exception or</span></span><a href="#l1932"></a>
<span id="l1933"><span class="c">#           return None</span></span><a href="#l1933"></a>
<span id="l1934"><span class="c">#     x.d = x.dst(), and assuming that doesn&#39;t raise an exception or</span></span><a href="#l1934"></a>
<span id="l1935"><span class="c">#           return None</span></span><a href="#l1935"></a>
<span id="l1936"><span class="c">#     x.s = x&#39;s standard offset, x.o - x.d</span></span><a href="#l1936"></a>
<span id="l1937"><span class="c">#</span></span><a href="#l1937"></a>
<span id="l1938"><span class="c"># Now some derived rules, where k is a duration (timedelta).</span></span><a href="#l1938"></a>
<span id="l1939"><span class="c">#</span></span><a href="#l1939"></a>
<span id="l1940"><span class="c"># 1. x.o = x.s + x.d</span></span><a href="#l1940"></a>
<span id="l1941"><span class="c">#    This follows from the definition of x.s.</span></span><a href="#l1941"></a>
<span id="l1942"><span class="c">#</span></span><a href="#l1942"></a>
<span id="l1943"><span class="c"># 2. If x and y have the same tzinfo member, x.s = y.s.</span></span><a href="#l1943"></a>
<span id="l1944"><span class="c">#    This is actually a requirement, an assumption we need to make about</span></span><a href="#l1944"></a>
<span id="l1945"><span class="c">#    sane tzinfo classes.</span></span><a href="#l1945"></a>
<span id="l1946"><span class="c">#</span></span><a href="#l1946"></a>
<span id="l1947"><span class="c"># 3. The naive UTC time corresponding to x is x.n - x.o.</span></span><a href="#l1947"></a>
<span id="l1948"><span class="c">#    This is again a requirement for a sane tzinfo class.</span></span><a href="#l1948"></a>
<span id="l1949"><span class="c">#</span></span><a href="#l1949"></a>
<span id="l1950"><span class="c"># 4. (x+k).s = x.s</span></span><a href="#l1950"></a>
<span id="l1951"><span class="c">#    This follows from #2, and that datimetimetz+timedelta preserves tzinfo.</span></span><a href="#l1951"></a>
<span id="l1952"><span class="c">#</span></span><a href="#l1952"></a>
<span id="l1953"><span class="c"># 5. (x+k).n = x.n + k</span></span><a href="#l1953"></a>
<span id="l1954"><span class="c">#    Again follows from how arithmetic is defined.</span></span><a href="#l1954"></a>
<span id="l1955"><span class="c">#</span></span><a href="#l1955"></a>
<span id="l1956"><span class="c"># Now we can explain tz.fromutc(x).  Let&#39;s assume it&#39;s an interesting case</span></span><a href="#l1956"></a>
<span id="l1957"><span class="c"># (meaning that the various tzinfo methods exist, and don&#39;t blow up or return</span></span><a href="#l1957"></a>
<span id="l1958"><span class="c"># None when called).</span></span><a href="#l1958"></a>
<span id="l1959"><span class="c">#</span></span><a href="#l1959"></a>
<span id="l1960"><span class="c"># The function wants to return a datetime y with timezone tz, equivalent to x.</span></span><a href="#l1960"></a>
<span id="l1961"><span class="c"># x is already in UTC.</span></span><a href="#l1961"></a>
<span id="l1962"><span class="c">#</span></span><a href="#l1962"></a>
<span id="l1963"><span class="c"># By #3, we want</span></span><a href="#l1963"></a>
<span id="l1964"><span class="c">#</span></span><a href="#l1964"></a>
<span id="l1965"><span class="c">#     y.n - y.o = x.n                             [1]</span></span><a href="#l1965"></a>
<span id="l1966"><span class="c">#</span></span><a href="#l1966"></a>
<span id="l1967"><span class="c"># The algorithm starts by attaching tz to x.n, and calling that y.  So</span></span><a href="#l1967"></a>
<span id="l1968"><span class="c"># x.n = y.n at the start.  Then it wants to add a duration k to y, so that [1]</span></span><a href="#l1968"></a>
<span id="l1969"><span class="c"># becomes true; in effect, we want to solve [2] for k:</span></span><a href="#l1969"></a>
<span id="l1970"><span class="c">#</span></span><a href="#l1970"></a>
<span id="l1971"><span class="c">#    (y+k).n - (y+k).o = x.n                      [2]</span></span><a href="#l1971"></a>
<span id="l1972"><span class="c">#</span></span><a href="#l1972"></a>
<span id="l1973"><span class="c"># By #1, this is the same as</span></span><a href="#l1973"></a>
<span id="l1974"><span class="c">#</span></span><a href="#l1974"></a>
<span id="l1975"><span class="c">#    (y+k).n - ((y+k).s + (y+k).d) = x.n          [3]</span></span><a href="#l1975"></a>
<span id="l1976"><span class="c">#</span></span><a href="#l1976"></a>
<span id="l1977"><span class="c"># By #5, (y+k).n = y.n + k, which equals x.n + k because x.n=y.n at the start.</span></span><a href="#l1977"></a>
<span id="l1978"><span class="c"># Substituting that into [3],</span></span><a href="#l1978"></a>
<span id="l1979"><span class="c">#</span></span><a href="#l1979"></a>
<span id="l1980"><span class="c">#    x.n + k - (y+k).s - (y+k).d = x.n; the x.n terms cancel, leaving</span></span><a href="#l1980"></a>
<span id="l1981"><span class="c">#    k - (y+k).s - (y+k).d = 0; rearranging,</span></span><a href="#l1981"></a>
<span id="l1982"><span class="c">#    k = (y+k).s - (y+k).d; by #4, (y+k).s == y.s, so</span></span><a href="#l1982"></a>
<span id="l1983"><span class="c">#    k = y.s - (y+k).d</span></span><a href="#l1983"></a>
<span id="l1984"><span class="c">#</span></span><a href="#l1984"></a>
<span id="l1985"><span class="c"># On the RHS, (y+k).d can&#39;t be computed directly, but y.s can be, and we</span></span><a href="#l1985"></a>
<span id="l1986"><span class="c"># approximate k by ignoring the (y+k).d term at first.  Note that k can&#39;t be</span></span><a href="#l1986"></a>
<span id="l1987"><span class="c"># very large, since all offset-returning methods return a duration of magnitude</span></span><a href="#l1987"></a>
<span id="l1988"><span class="c"># less than 24 hours.  For that reason, if y is firmly in std time, (y+k).d must</span></span><a href="#l1988"></a>
<span id="l1989"><span class="c"># be 0, so ignoring it has no consequence then.</span></span><a href="#l1989"></a>
<span id="l1990"><span class="c">#</span></span><a href="#l1990"></a>
<span id="l1991"><span class="c"># In any case, the new value is</span></span><a href="#l1991"></a>
<span id="l1992"><span class="c">#</span></span><a href="#l1992"></a>
<span id="l1993"><span class="c">#     z = y + y.s                                 [4]</span></span><a href="#l1993"></a>
<span id="l1994"><span class="c">#</span></span><a href="#l1994"></a>
<span id="l1995"><span class="c"># It&#39;s helpful to step back at look at [4] from a higher level:  it&#39;s simply</span></span><a href="#l1995"></a>
<span id="l1996"><span class="c"># mapping from UTC to tz&#39;s standard time.</span></span><a href="#l1996"></a>
<span id="l1997"><span class="c">#</span></span><a href="#l1997"></a>
<span id="l1998"><span class="c"># At this point, if</span></span><a href="#l1998"></a>
<span id="l1999"><span class="c">#</span></span><a href="#l1999"></a>
<span id="l2000"><span class="c">#     z.n - z.o = x.n                             [5]</span></span><a href="#l2000"></a>
<span id="l2001"><span class="c">#</span></span><a href="#l2001"></a>
<span id="l2002"><span class="c"># we have an equivalent time, and are almost done.  The insecurity here is</span></span><a href="#l2002"></a>
<span id="l2003"><span class="c"># at the start of daylight time.  Picture US Eastern for concreteness.  The wall</span></span><a href="#l2003"></a>
<span id="l2004"><span class="c"># time jumps from 1:59 to 3:00, and wall hours of the form 2:MM don&#39;t make good</span></span><a href="#l2004"></a>
<span id="l2005"><span class="c"># sense then.  The docs ask that an Eastern tzinfo class consider such a time to</span></span><a href="#l2005"></a>
<span id="l2006"><span class="c"># be EDT (because it&#39;s &quot;after 2&quot;), which is a redundant spelling of 1:MM EST</span></span><a href="#l2006"></a>
<span id="l2007"><span class="c"># on the day DST starts.  We want to return the 1:MM EST spelling because that&#39;s</span></span><a href="#l2007"></a>
<span id="l2008"><span class="c"># the only spelling that makes sense on the local wall clock.</span></span><a href="#l2008"></a>
<span id="l2009"><span class="c">#</span></span><a href="#l2009"></a>
<span id="l2010"><span class="c"># In fact, if [5] holds at this point, we do have the standard-time spelling,</span></span><a href="#l2010"></a>
<span id="l2011"><span class="c"># but that takes a bit of proof.  We first prove a stronger result.  What&#39;s the</span></span><a href="#l2011"></a>
<span id="l2012"><span class="c"># difference between the LHS and RHS of [5]?  Let</span></span><a href="#l2012"></a>
<span id="l2013"><span class="c">#</span></span><a href="#l2013"></a>
<span id="l2014"><span class="c">#     diff = x.n - (z.n - z.o)                    [6]</span></span><a href="#l2014"></a>
<span id="l2015"><span class="c">#</span></span><a href="#l2015"></a>
<span id="l2016"><span class="c"># Now</span></span><a href="#l2016"></a>
<span id="l2017"><span class="c">#     z.n =                       by [4]</span></span><a href="#l2017"></a>
<span id="l2018"><span class="c">#     (y + y.s).n =               by #5</span></span><a href="#l2018"></a>
<span id="l2019"><span class="c">#     y.n + y.s =                 since y.n = x.n</span></span><a href="#l2019"></a>
<span id="l2020"><span class="c">#     x.n + y.s =                 since z and y are have the same tzinfo member,</span></span><a href="#l2020"></a>
<span id="l2021"><span class="c">#                                     y.s = z.s by #2</span></span><a href="#l2021"></a>
<span id="l2022"><span class="c">#     x.n + z.s</span></span><a href="#l2022"></a>
<span id="l2023"><span class="c">#</span></span><a href="#l2023"></a>
<span id="l2024"><span class="c"># Plugging that back into [6] gives</span></span><a href="#l2024"></a>
<span id="l2025"><span class="c">#</span></span><a href="#l2025"></a>
<span id="l2026"><span class="c">#     diff =</span></span><a href="#l2026"></a>
<span id="l2027"><span class="c">#     x.n - ((x.n + z.s) - z.o) =     expanding</span></span><a href="#l2027"></a>
<span id="l2028"><span class="c">#     x.n - x.n - z.s + z.o =         cancelling</span></span><a href="#l2028"></a>
<span id="l2029"><span class="c">#     - z.s + z.o =                   by #2</span></span><a href="#l2029"></a>
<span id="l2030"><span class="c">#     z.d</span></span><a href="#l2030"></a>
<span id="l2031"><span class="c">#</span></span><a href="#l2031"></a>
<span id="l2032"><span class="c"># So diff = z.d.</span></span><a href="#l2032"></a>
<span id="l2033"><span class="c">#</span></span><a href="#l2033"></a>
<span id="l2034"><span class="c"># If [5] is true now, diff = 0, so z.d = 0 too, and we have the standard-time</span></span><a href="#l2034"></a>
<span id="l2035"><span class="c"># spelling we wanted in the endcase described above.  We&#39;re done.  Contrarily,</span></span><a href="#l2035"></a>
<span id="l2036"><span class="c"># if z.d = 0, then we have a UTC equivalent, and are also done.</span></span><a href="#l2036"></a>
<span id="l2037"><span class="c">#</span></span><a href="#l2037"></a>
<span id="l2038"><span class="c"># If [5] is not true now, diff = z.d != 0, and z.d is the offset we need to</span></span><a href="#l2038"></a>
<span id="l2039"><span class="c"># add to z (in effect, z is in tz&#39;s standard time, and we need to shift the</span></span><a href="#l2039"></a>
<span id="l2040"><span class="c"># local clock into tz&#39;s daylight time).</span></span><a href="#l2040"></a>
<span id="l2041"><span class="c">#</span></span><a href="#l2041"></a>
<span id="l2042"><span class="c"># Let</span></span><a href="#l2042"></a>
<span id="l2043"><span class="c">#</span></span><a href="#l2043"></a>
<span id="l2044"><span class="c">#     z&#39; = z + z.d = z + diff                     [7]</span></span><a href="#l2044"></a>
<span id="l2045"><span class="c">#</span></span><a href="#l2045"></a>
<span id="l2046"><span class="c"># and we can again ask whether</span></span><a href="#l2046"></a>
<span id="l2047"><span class="c">#</span></span><a href="#l2047"></a>
<span id="l2048"><span class="c">#     z&#39;.n - z&#39;.o = x.n                           [8]</span></span><a href="#l2048"></a>
<span id="l2049"><span class="c">#</span></span><a href="#l2049"></a>
<span id="l2050"><span class="c"># If so, we&#39;re done.  If not, the tzinfo class is insane, according to the</span></span><a href="#l2050"></a>
<span id="l2051"><span class="c"># assumptions we&#39;ve made.  This also requires a bit of proof.  As before, let&#39;s</span></span><a href="#l2051"></a>
<span id="l2052"><span class="c"># compute the difference between the LHS and RHS of [8] (and skipping some of</span></span><a href="#l2052"></a>
<span id="l2053"><span class="c"># the justifications for the kinds of substitutions we&#39;ve done several times</span></span><a href="#l2053"></a>
<span id="l2054"><span class="c"># already):</span></span><a href="#l2054"></a>
<span id="l2055"><span class="c">#</span></span><a href="#l2055"></a>
<span id="l2056"><span class="c">#     diff&#39; = x.n - (z&#39;.n - z&#39;.o) =           replacing z&#39;.n via [7]</span></span><a href="#l2056"></a>
<span id="l2057"><span class="c">#             x.n  - (z.n + diff - z&#39;.o) =    replacing diff via [6]</span></span><a href="#l2057"></a>
<span id="l2058"><span class="c">#             x.n - (z.n + x.n - (z.n - z.o) - z&#39;.o) =</span></span><a href="#l2058"></a>
<span id="l2059"><span class="c">#             x.n - z.n - x.n + z.n - z.o + z&#39;.o =    cancel x.n</span></span><a href="#l2059"></a>
<span id="l2060"><span class="c">#             - z.n + z.n - z.o + z&#39;.o =              cancel z.n</span></span><a href="#l2060"></a>
<span id="l2061"><span class="c">#             - z.o + z&#39;.o =                      #1 twice</span></span><a href="#l2061"></a>
<span id="l2062"><span class="c">#             -z.s - z.d + z&#39;.s + z&#39;.d =          z and z&#39; have same tzinfo</span></span><a href="#l2062"></a>
<span id="l2063"><span class="c">#             z&#39;.d - z.d</span></span><a href="#l2063"></a>
<span id="l2064"><span class="c">#</span></span><a href="#l2064"></a>
<span id="l2065"><span class="c"># So z&#39; is UTC-equivalent to x iff z&#39;.d = z.d at this point.  If they are equal,</span></span><a href="#l2065"></a>
<span id="l2066"><span class="c"># we&#39;ve found the UTC-equivalent so are done.  In fact, we stop with [7] and</span></span><a href="#l2066"></a>
<span id="l2067"><span class="c"># return z&#39;, not bothering to compute z&#39;.d.</span></span><a href="#l2067"></a>
<span id="l2068"><span class="c">#</span></span><a href="#l2068"></a>
<span id="l2069"><span class="c"># How could z.d and z&#39;d differ?  z&#39; = z + z.d [7], so merely moving z&#39; by</span></span><a href="#l2069"></a>
<span id="l2070"><span class="c"># a dst() offset, and starting *from* a time already in DST (we know z.d != 0),</span></span><a href="#l2070"></a>
<span id="l2071"><span class="c"># would have to change the result dst() returns:  we start in DST, and moving</span></span><a href="#l2071"></a>
<span id="l2072"><span class="c"># a little further into it takes us out of DST.</span></span><a href="#l2072"></a>
<span id="l2073"><span class="c">#</span></span><a href="#l2073"></a>
<span id="l2074"><span class="c"># There isn&#39;t a sane case where this can happen.  The closest it gets is at</span></span><a href="#l2074"></a>
<span id="l2075"><span class="c"># the end of DST, where there&#39;s an hour in UTC with no spelling in a hybrid</span></span><a href="#l2075"></a>
<span id="l2076"><span class="c"># tzinfo class.  In US Eastern, that&#39;s 5:MM UTC = 0:MM EST = 1:MM EDT.  During</span></span><a href="#l2076"></a>
<span id="l2077"><span class="c"># that hour, on an Eastern clock 1:MM is taken as being in standard time (6:MM</span></span><a href="#l2077"></a>
<span id="l2078"><span class="c"># UTC) because the docs insist on that, but 0:MM is taken as being in daylight</span></span><a href="#l2078"></a>
<span id="l2079"><span class="c"># time (4:MM UTC).  There is no local time mapping to 5:MM UTC.  The local</span></span><a href="#l2079"></a>
<span id="l2080"><span class="c"># clock jumps from 1:59 back to 1:00 again, and repeats the 1:MM hour in</span></span><a href="#l2080"></a>
<span id="l2081"><span class="c"># standard time.  Since that&#39;s what the local clock *does*, we want to map both</span></span><a href="#l2081"></a>
<span id="l2082"><span class="c"># UTC hours 5:MM and 6:MM to 1:MM Eastern.  The result is ambiguous</span></span><a href="#l2082"></a>
<span id="l2083"><span class="c"># in local time, but so it goes -- it&#39;s the way the local clock works.</span></span><a href="#l2083"></a>
<span id="l2084"><span class="c">#</span></span><a href="#l2084"></a>
<span id="l2085"><span class="c"># When x = 5:MM UTC is the input to this algorithm, x.o=0, y.o=-5 and y.d=0,</span></span><a href="#l2085"></a>
<span id="l2086"><span class="c"># so z=0:MM.  z.d=60 (minutes) then, so [5] doesn&#39;t hold and we keep going.</span></span><a href="#l2086"></a>
<span id="l2087"><span class="c"># z&#39; = z + z.d = 1:MM then, and z&#39;.d=0, and z&#39;.d - z.d = -60 != 0 so [8]</span></span><a href="#l2087"></a>
<span id="l2088"><span class="c"># (correctly) concludes that z&#39; is not UTC-equivalent to x.</span></span><a href="#l2088"></a>
<span id="l2089"><span class="c">#</span></span><a href="#l2089"></a>
<span id="l2090"><span class="c"># Because we know z.d said z was in daylight time (else [5] would have held and</span></span><a href="#l2090"></a>
<span id="l2091"><span class="c"># we would have stopped then), and we know z.d != z&#39;.d (else [8] would have held</span></span><a href="#l2091"></a>
<span id="l2092"><span class="c"># and we have stopped then), and there are only 2 possible values dst() can</span></span><a href="#l2092"></a>
<span id="l2093"><span class="c"># return in Eastern, it follows that z&#39;.d must be 0 (which it is in the example,</span></span><a href="#l2093"></a>
<span id="l2094"><span class="c"># but the reasoning doesn&#39;t depend on the example -- it depends on there being</span></span><a href="#l2094"></a>
<span id="l2095"><span class="c"># two possible dst() outcomes, one zero and the other non-zero).  Therefore</span></span><a href="#l2095"></a>
<span id="l2096"><span class="c"># z&#39; must be in standard time, and is the spelling we want in this case.</span></span><a href="#l2096"></a>
<span id="l2097"><span class="c">#</span></span><a href="#l2097"></a>
<span id="l2098"><span class="c"># Note again that z&#39; is not UTC-equivalent as far as the hybrid tzinfo class is</span></span><a href="#l2098"></a>
<span id="l2099"><span class="c"># concerned (because it takes z&#39; as being in standard time rather than the</span></span><a href="#l2099"></a>
<span id="l2100"><span class="c"># daylight time we intend here), but returning it gives the real-life &quot;local</span></span><a href="#l2100"></a>
<span id="l2101"><span class="c"># clock repeats an hour&quot; behavior when mapping the &quot;unspellable&quot; UTC hour into</span></span><a href="#l2101"></a>
<span id="l2102"><span class="c"># tz.</span></span><a href="#l2102"></a>
<span id="l2103"><span class="c">#</span></span><a href="#l2103"></a>
<span id="l2104"><span class="c"># When the input is 6:MM, z=1:MM and z.d=0, and we stop at once, again with</span></span><a href="#l2104"></a>
<span id="l2105"><span class="c"># the 1:MM standard time spelling we want.</span></span><a href="#l2105"></a>
<span id="l2106"><span class="c">#</span></span><a href="#l2106"></a>
<span id="l2107"><span class="c"># So how can this break?  One of the assumptions must be violated.  Two</span></span><a href="#l2107"></a>
<span id="l2108"><span class="c"># possibilities:</span></span><a href="#l2108"></a>
<span id="l2109"><span class="c">#</span></span><a href="#l2109"></a>
<span id="l2110"><span class="c"># 1) [2] effectively says that y.s is invariant across all y belong to a given</span></span><a href="#l2110"></a>
<span id="l2111"><span class="c">#    time zone.  This isn&#39;t true if, for political reasons or continental drift,</span></span><a href="#l2111"></a>
<span id="l2112"><span class="c">#    a region decides to change its base offset from UTC.</span></span><a href="#l2112"></a>
<span id="l2113"><span class="c">#</span></span><a href="#l2113"></a>
<span id="l2114"><span class="c"># 2) There may be versions of &quot;double daylight&quot; time where the tail end of</span></span><a href="#l2114"></a>
<span id="l2115"><span class="c">#    the analysis gives up a step too early.  I haven&#39;t thought about that</span></span><a href="#l2115"></a>
<span id="l2116"><span class="c">#    enough to say.</span></span><a href="#l2116"></a>
<span id="l2117"><span class="c">#</span></span><a href="#l2117"></a>
<span id="l2118"><span class="c"># In any case, it&#39;s clear that the default fromutc() is strong enough to handle</span></span><a href="#l2118"></a>
<span id="l2119"><span class="c"># &quot;almost all&quot; time zones:  so long as the standard offset is invariant, it</span></span><a href="#l2119"></a>
<span id="l2120"><span class="c"># doesn&#39;t matter if daylight time transition points change from year to year, or</span></span><a href="#l2120"></a>
<span id="l2121"><span class="c"># if daylight time is skipped in some years; it doesn&#39;t matter how large or</span></span><a href="#l2121"></a>
<span id="l2122"><span class="c"># small dst() may get within its bounds; and it doesn&#39;t even matter if some</span></span><a href="#l2122"></a>
<span id="l2123"><span class="c"># perverse time zone returns a negative dst()).  So a breaking case must be</span></span><a href="#l2123"></a>
<span id="l2124"><span class="c"># pretty bizarre, and a tzinfo subclass can override fromutc() if it is.</span></span><a href="#l2124"></a>
<span id="l2125"></span><a href="#l2125"></a>
<span id="l2126"><span class="k">try</span><span class="p">:</span></span><a href="#l2126"></a>
<span id="l2127">    <span class="kn">from</span> <span class="nn">_datetime</span> <span class="kn">import</span> <span class="o">*</span></span><a href="#l2127"></a>
<span id="l2128"><span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span></span><a href="#l2128"></a>
<span id="l2129">    <span class="k">pass</span></span><a href="#l2129"></a>
<span id="l2130"><span class="k">else</span><span class="p">:</span></span><a href="#l2130"></a>
<span id="l2131">    <span class="c"># Clean up unused names</span></span><a href="#l2131"></a>
<span id="l2132">    <span class="k">del</span> <span class="p">(</span><span class="n">_DAYNAMES</span><span class="p">,</span> <span class="n">_DAYS_BEFORE_MONTH</span><span class="p">,</span> <span class="n">_DAYS_IN_MONTH</span><span class="p">,</span> <span class="n">_DI100Y</span><span class="p">,</span> <span class="n">_DI400Y</span><span class="p">,</span></span><a href="#l2132"></a>
<span id="l2133">         <span class="n">_DI4Y</span><span class="p">,</span> <span class="n">_EPOCH</span><span class="p">,</span> <span class="n">_MAXORDINAL</span><span class="p">,</span> <span class="n">_MONTHNAMES</span><span class="p">,</span> <span class="n">_build_struct_time</span><span class="p">,</span></span><a href="#l2133"></a>
<span id="l2134">         <span class="n">_check_date_fields</span><span class="p">,</span> <span class="n">_check_int_field</span><span class="p">,</span> <span class="n">_check_time_fields</span><span class="p">,</span></span><a href="#l2134"></a>
<span id="l2135">         <span class="n">_check_tzinfo_arg</span><span class="p">,</span> <span class="n">_check_tzname</span><span class="p">,</span> <span class="n">_check_utc_offset</span><span class="p">,</span> <span class="n">_cmp</span><span class="p">,</span> <span class="n">_cmperror</span><span class="p">,</span></span><a href="#l2135"></a>
<span id="l2136">         <span class="n">_date_class</span><span class="p">,</span> <span class="n">_days_before_month</span><span class="p">,</span> <span class="n">_days_before_year</span><span class="p">,</span> <span class="n">_days_in_month</span><span class="p">,</span></span><a href="#l2136"></a>
<span id="l2137">         <span class="n">_format_time</span><span class="p">,</span> <span class="n">_is_leap</span><span class="p">,</span> <span class="n">_isoweek1monday</span><span class="p">,</span> <span class="n">_math</span><span class="p">,</span> <span class="n">_ord2ymd</span><span class="p">,</span></span><a href="#l2137"></a>
<span id="l2138">         <span class="n">_time</span><span class="p">,</span> <span class="n">_time_class</span><span class="p">,</span> <span class="n">_tzinfo_class</span><span class="p">,</span> <span class="n">_wrap_strftime</span><span class="p">,</span> <span class="n">_ymd2ord</span><span class="p">)</span></span><a href="#l2138"></a>
<span id="l2139">    <span class="c"># XXX Since import * above excludes names that start with _,</span></span><a href="#l2139"></a>
<span id="l2140">    <span class="c"># docstring does not get overwritten. In the future, it may be</span></span><a href="#l2140"></a>
<span id="l2141">    <span class="c"># appropriate to maintain a single module level docstring and</span></span><a href="#l2141"></a>
<span id="l2142">    <span class="c"># remove the following line.</span></span><a href="#l2142"></a>
<span id="l2143">    <span class="kn">from</span> <span class="nn">_datetime</span> <span class="kn">import</span> <span class="n">__doc__</span></span><a href="#l2143"></a></pre>
<div class="sourcelast"></div>
</div>
</div>
</div>

<script type="text/javascript">process_dates()</script>


</body>
</html>

