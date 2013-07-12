<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fwi="http://www.christophermchurch.com">
<xsl:output method="html" version="4.0" encoding="UTF-8" indent="yes" doctype-system="about:legacy-compat"/>
<xsl:template match="/">
  <html>
  <head>
  <script src="http://code.jquery.com/jquery-latest.min.js" type="text/javascript"></script>
	<style type="text/css">
		* {font-family:Arial, Helvetica, sans-serif;}
		
		#page-wrapper {
			margin:auto;
			padding:25px;
			width:900px;
			background-color:#f0f0f0;
			border-radius:15px;
		}
		#file-details {margin-right:0px; margin-left:auto;width:400px;border-style:solid; border-width:2px;border-radius:15px; background-color:#f7f7f7; padding:5px;float:right;}
		#file-details select {width:inherit;}
		#metadata-wrapper td { padding-right:2px; }
		#metadata-wrapper table {  width:inherit;}
		.item {margin-left:1%; margin-right:1%;}
		.body {margin-left:2%; margin-right:1%;}
		
		#table-of-contents, #document-notes {float:left;margin-left:1%;width:450px;}
		a:hover {color:black;}
		a {color:#2F4F4F;}
		
		.center {margin:auto; text-align:center;}
		
		#header h1,#header h4 {line-height:5px;margin-bottom:0px;}
			
		#metadata-wrapper {
			background-color: #FFF;
			height: auto;
			overflow: auto;
			padding: 3px;
			border-radius: 15px;
			border-weight: 1px;
			border-style: solid;
		}
		.clear {clear:both;}
		.illegible {color:#FF0000;}
		.sic {color:#CCCC00;}
		#content-wrapper {position:relative;}
		.notes {background:#f7f7f7;width:inherit;padding:15px;border-radius:15px;margin-left:10px;margin-right:10px;}
		.notes ul {margin:inherit;}
		.author {font-style:italic;color:grey;}
		.quote p {font-size:14px;padding-left:25px;padding-right:100px;text-align:justify;}
	</style>
	<script>
	  var current_location = window.location.pathname.split('/').pop();
	</script>
  </head>
  <body>
 		<div id="page-wrapper">
		<a id="top"/>
		<div id="metadata-wrapper">
		  <div id="header">
			  <h1>Late 19th Century Caribbean Disasters</h1>
			  <h4>C. Church, Y. Lin -- University of Califoria, Berkeley -- 2013</h4>
			  <hr/>
		  </div>
		  <div id="table-of-contents">
			  <h4>Table of Contents</h4>
			  <xsl:for-each select="fwi:issue/fwi:item"> 	
					<a>
						<xsl:variable name="item-id" select="count(preceding-sibling::fwi:item)+1" />
						<xsl:attribute name="href">#item-<xsl:value-of select="$item-id"/></xsl:attribute>
						<xsl:value-of select="$item-id"/> - 
						<xsl:choose>
									<xsl:when test="fwi:title!=''"><xsl:value-of select="fwi:title"/> - [<xsl:value-of select="./@type"/>]</xsl:when>
									<xsl:otherwise>Untitled - [<xsl:value-of select="./@type"/>]</xsl:otherwise>
						</xsl:choose>
					</a>
					<br/>
			  </xsl:for-each>
		  </div>
		  
		  <div id="file-details">
				
				<select onchange="location = this.options[this.selectedIndex].value;">
					<option value="">Select another xml file...</option>
					<xsl:for-each select="document('filetree.txt')/filetree/fpath">
						<option><xsl:attribute name="value"><xsl:value-of select="."/></xsl:attribute><xsl:value-of select="."/></option>
					</xsl:for-each>
    			</select>		  
				<table>
					<tbody>
					  <tr><td><h4>Current XML</h4></td><td id="current-file"></td></tr><script type="text/javascript">document.getElementById('current-file').innerHTML=current_location;</script>
					  <tr><td><h4>Newspaper:</h4></td><td><xsl:value-of select="fwi:issue/fwi:metadata/fwi:newspaper/@name"/></td></tr>
					  <tr><td><h4>Date:</h4></td><td><xsl:value-of select="fwi:issue/fwi:metadata/fwi:newspaper/@date"/></td></tr>
					  <tr><td><h4>Folder:</h4></td><td><xsl:value-of select="fwi:issue/fwi:metadata/fwi:files/@folder"/></td></tr>
					  <tr><td><h4>Files:</h4></td><td><xsl:for-each select="fwi:issue/fwi:metadata/fwi:files/fwi:file"><xsl:value-of select="./@name"/><br/></xsl:for-each></td></tr>
					</tbody>
				</table>
		  </div>
		  
		  <div id="document-notes">
		    <h4>Notes</h4>
			<ul><xsl:for-each select="fwi:issue/fwi:metadata/fwi:notes/fwi:note"><li><xsl:value-of select="."/> - <span class="author"><xsl:value-of select="./@author"/></span></li></xsl:for-each></ul>
		  </div>
		  <button onclick="var w = window.open();var text = $('.body p').text();$(w.document.body).html(text);">Export all paragraph text</button>
		  <span class="clear"/>
		</div>
		
		  
		<div id="content-wrapper">
			<xsl:for-each select="fwi:issue/fwi:item"> 	
				<a><xsl:attribute name="id">item-<xsl:value-of select="count(preceding-sibling::fwi:item)+1"/></xsl:attribute></a>
				<div class="item">
					<h2>
						<xsl:choose>
							<xsl:when test="fwi:title!=''"><xsl:value-of select="fwi:title"/> - [<xsl:value-of select="./@type"/>]</xsl:when>
							<xsl:otherwise>Untitled - [<xsl:value-of select="./@type"/>]</xsl:otherwise>
						</xsl:choose>
						
					</h2>
					
					<xsl:choose>
						<xsl:when test="fwi:notes!=''">
							<div class="notes">
							 <ul>	
								<xsl:for-each select="fwi:notes/fwi:note">
									<li><xsl:value-of select="."/> - <span class="author"><xsl:value-of select="./@author"/></span></li>
								</xsl:for-each>
							 </ul>
							</div>
						</xsl:when>
					</xsl:choose>
					
					<div class="body">
						<xsl:for-each select="fwi:body/fwi:section">
							<xsl:apply-templates/>
							
							<hr/>
						</xsl:for-each>
					</div>
				<div class="center"><a href="#top" class="to-top-link">- to top -</a></div>
				</div>					
			  </xsl:for-each>
		</div>
	 </div>   
  </body>
  </html>
</xsl:template>

<xsl:template match="fwi:illegible">
	
	<span class="illegible">[illegible]<xsl:text> </xsl:text><xsl:apply-templates/></span>
	
</xsl:template>

<xsl:template match="fwi:para">
				<div>					
									<xsl:attribute name="id">item-<xsl:value-of select="count(../../../preceding-sibling::item)+1"/>_sect-<xsl:value-of select="../@num"/>_para-<xsl:value-of select="./@num"/></xsl:attribute>
									<p>
									<xsl:apply-templates/>
									</p>
								</div>
</xsl:template>

<xsl:template match="fwi:heading">
	<h3><xsl:apply-templates/></h3>
</xsl:template>

<xsl:template match="fwi:quote">
	
	<div class="quote">
				<xsl:apply-templates/>
	</div>
	
</xsl:template>

<xsl:template match="fwi:sic">
	
	<span class="sic">[sic]<xsl:text> </xsl:text><xsl:apply-templates/></span>
	
</xsl:template>

</xsl:stylesheet>

