# ruff: noqa: E501
"""Small synthetic pages in the layout of populi.co/api, for the edge cases."""

INDEX = """<html><body>
<div class="toc-wrapper"><ul>
  <li><a href="models/widgets.html" class="toc-h1 toc-link" data-title="Widget">Widget</a></li>
  <li><a href="models/webhooks.html" class="toc-h1 toc-link" data-title="Webhooks">Webhooks</a></li>
</ul></div>
<div class="content">
<h1 id="introduction">Introduction</h1>
<p>See <a href="models/widgets.html#index">widgets</a>.</p>
<aside class="notice">This documentation updated on 2026-09-21 11:05:10 PST</aside>
<h1 id="filters">Filter conditions for reports</h1>
<div class="highlight"><pre class="highlight plaintext"><code>GET /people</code></pre></div>
</div></body></html>"""

WIDGETS = """<html><body><div class="content">
<h1 id="widget">Widget</h1>
<p>A widget belongs to a <a href="people.html#show">person</a>.</p>
<h2 id="the-widget-object">The Widget object</h2>
<blockquote><p>The Widget object looks like this in JSON:</p></blockquote>
<div class="highlight"><pre class="highlight json tab-json"><code>{"object": "widget", "id": 1}</code></pre></div>
<table><thead><tr><th>Attribute</th><th>Required</th><th>Data Type</th></tr></thead>
<tbody><tr><td>id</td><td>Yes</td><td>int</td></tr>
<tr><td>name</td><td>No</td><td>text (50)</td></tr></tbody></table>
<h2 id="index">index</h2>
<blockquote><p>Example code to call this method:</p></blockquote>
<div class="highlight"><pre class="highlight shell tab-shell"><code>curl "https://yourschool.populiweb.com/api2/widgets"</code></pre></div>
<div class="highlight"><pre class="highlight ruby tab-ruby"><code>HTTParty.get('...')</code></pre></div>
<div class="highlight"><pre class="highlight python tab-python"><code>requests.get('...')</code></pre></div>
<blockquote><p>Example response:</p></blockquote>
<div class="highlight"><pre class="highlight json tab-json"><code>{"object": "list"}</code></pre></div>
<p>Retrieves all Widget objects. Uses the <code>filter</code> | parameter.</p>
<h3 id="http-request">HTTP Request</h3>
<p><code>GET /widgets</code></p>
<h3 id="parameters">Parameters</h3>
<table><thead><tr><th>Name</th><th>Required</th><th>Data Type</th><th>Description</th></tr></thead>
<tbody><tr><td>filter</td><td>No</td><td>mixed</td><td>See available filter conditions</td></tr>
<tr><td>page</td><td>No</td><td>int</td><td>The page of results</td></tr></tbody></table>
<h3 id="filter-condition-parameters">Filter Condition Parameters</h3>
<table><thead><tr><th>Name</th><th>Type</th></tr></thead>
<tbody><tr><td>added_at</td><td>datetime</td></tr></tbody></table>
<h3 id="expandable-properties">Expandable Properties</h3>
<ul><li>owner</li><li>tags</li></ul>
<h3 id="permissions">Permissions</h3>
<p>One of the following roles is required to call this method:</p>
<ul><li>Registrar</li><li>Academic Admin</li></ul>
<h2 id="show">show</h2>
<p>Retrieves a specific Widget object.</p>
<h3 id="http-request-2">HTTP Request</h3>
<p><code>GET /widgets/(widget)</code></p>
<h3 id="parameters-2">Parameters</h3>
<p>None</p>
<h3 id="rate-notes">Rate Notes</h3>
<p>Slow.</p>
</div></body></html>"""

WEBHOOKS = """<html><body><div class="content">
<h1 id="webhooks">Webhooks</h1>
<p>Webhooks send information to your applications.</p>
<h2 id="available-events">Available events</h2>
<table><thead><tr><th>Event</th><th>Name</th></tr></thead>
<tbody><tr><td><code>term_updated</code></td><td>Academic Term Updated</td></tr>
<tr><td><code>person_created</code></td><td>Person Added</td></tr></tbody></table>
<h2 id="academic-term-updated">Academic Term Updated</h2>
<p>Whenever an academic term is updated.</p>
<div class="highlight"><pre class="highlight json tab-json"><code>{"event": "term_updated"}</code></pre></div>
<h2 id="person-added">Person Added</h2>
<p>Whenever a person is added.</p>
<div class="highlight"><pre class="highlight json tab-json"><code>{"event": "person_created"}</code></pre></div>
</div></body></html>"""
