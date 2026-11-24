const test = require('node:test');
const assert = require('node:assert/strict');
const escapeHtml = require('../escapeHtml');

test('escapes HTML-special characters before rendering form results', () => {
  assert.equal(escapeHtml(`<script src="x">&'`), '&lt;script src=&quot;x&quot;&gt;&amp;&#39;');
});

test('converts non-string values to text', () => {
  assert.equal(escapeHtml(42), '42');
});
