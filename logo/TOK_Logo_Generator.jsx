#target illustrator

(function() {
    var doc = app.documents.add(DocumentColorSpace.RGB, 600, 600);
    doc.name = "TOK_Logo_v3";
    
    // === COLORS ===
    var bg = new RGBColor();
    bg.red = 10; bg.green = 10; bg.blue = 15;
    
    var cyan = new RGBColor();
    cyan.red = 37; cyan.green = 244; cyan.blue = 238;
    
    var pink = new RGBColor();
    pink.red = 254; pink.green = 44; pink.blue = 85;
    
    var white = new RGBColor();
    white.red = 255; white.green = 255; white.blue = 255;
    
    var gold = new RGBColor();
    gold.red = 255; gold.green = 215; gold.blue = 0;
    
    var noColor = new NoColor();
    
    // === BACKGROUND ===
    var bgRect = doc.pathItems.rectangle(0, 0, 600, 600);
    bgRect.filled = true;
    bgRect.fillColor = bg;
    bgRect.stroked = false;
    
    // === DIAMOND BORDER ===
    var diamond = doc.pathItems.add();
    diamond.setEntirePath([[300, 560], [560, 300], [300, 40], [40, 300]]);
    diamond.closed = true;
    diamond.filled = false;
    diamond.stroked = true;
    diamond.strokeColor = cyan;
    diamond.strokeWidth = 3;
    
    // === CORNER ACCENTS ===
    function corner(x1, y1, x2, y2, color) {
        var c = doc.pathItems.add();
        c.setEntirePath([[x1, y1], [x2, y2]]);
        c.filled = false;
        c.stroked = true;
        c.strokeColor = color;
        c.strokeWidth = 2;
    }
    corner(80, 80, 120, 80, cyan);
    corner(80, 80, 80, 120, cyan);
    corner(480, 80, 520, 80, pink);
    corner(520, 80, 520, 120, pink);
    corner(80, 480, 80, 520, pink);
    corner(80, 520, 120, 520, pink);
    corner(520, 480, 520, 520, cyan);
    corner(480, 520, 520, 520, cyan);
    
    // === TIKTOK MUSIC NOTE ===
    // Note head (ellipse)
    var noteHead = doc.pathItems.ellipse(215, 340, 30, 22);
    noteHead.filled = true;
    noteHead.fillColor = pink;
    noteHead.stroked = false;
    
    var noteHeadCyan = doc.pathItems.ellipse(215, 337, 30, 22);
    noteHeadCyan.filled = true;
    noteHeadCyan.fillColor = cyan;
    noteHeadCyan.stroked = false;
    
    // Note stem
    var stem = doc.pathItems.add();
    stem.setEntirePath([[355, 200], [355, 135]]);
    stem.stroked = true;
    stem.strokeColor = cyan;
    stroke = stem.strokeColor;
    stem.strokeWidth = 8;
    stem.filled = false;
    
    var stemPink = doc.pathItems.add();
    stemPink.setEntirePath([[358, 200], [358, 135]]);
    stemPink.stroked = true;
    stemPink.strokeColor = pink;
    stemPink.strokeWidth = 8;
    stemPink.filled = false;
    
    // Note flag
    var flag = doc.pathItems.add();
    flag.setEntirePath([[355, 135], [380, 125], [380, 155]]);
    flag.closed = true;
    flag.filled = true;
    flag.fillColor = cyan;
    flag.stroked = false;
    
    // === TOK TEXT — 3 LAYERS FOR GLITCH/GLOW EFFECT ===
    
    function makeText(text, x, y, size, fillColor, strokeCol, strokeW) {
        var ti = doc.textItems.add();
        ti.contents = text;
        ti.position = [x, y];
        var attr = ti.textRange.characterAttributes;
        attr.size = size;
        attr.fillColor = fillColor;
        if (strokeCol) {
            attr.strokeColor = strokeCol;
            attr.strokeWidth = strokeW || 2;
        } else {
            attr.strokeColor = noColor;
        }
        try { attr.textFont = app.textFonts.getByName("ArialBlack"); } catch(e) {}
        return ti;
    }
    
    // Cyan offset layer (shifted left)
    makeText("TOK", 155, 410, 180, cyan, null, 0);
    // Pink offset layer (shifted right)
    makeText("TOK", 175, 410, 180, pink, null, 0);
    // Main white text with pink outline
    makeText("TOK", 165, 410, 180, white, pink, 3);
    
    // === TAGLINE ===
    makeText("T I K T O K   A G E N C Y", 175, 460, 22, cyan, null, 0);
    
    // === DECORATIVE DOTS ===
    var dotData = [
        [200, 490, 4, cyan],
        [220, 490, 3, pink],
        [238, 490, 2, white],
        [382, 490, 2, white],
        [400, 490, 3, pink],
        [420, 490, 4, cyan]
    ];
    for (var i = 0; i < dotData.length; i++) {
        var d = dotData[i];
        var dot = doc.pathItems.ellipse(d[1] + d[2], d[0] - d[2], d[2]*2, d[2]*2);
        dot.filled = true;
        dot.fillColor = d[3];
        dot.stroked = false;
    }
    
    // Reorder: bring text to front
    bgRect.zOrder(ZOrderMethod.SENDTOBACK);
    diamond.zOrder(ZOrderMethod.BRINGFORWARD);
    
    // === SAVE AI FILE ===
    var aiPath = "C:/Gab/work/Tiktok Managing Agency/logo/TOK_Logo_v3.ai";
    var saveOpts = new IllustratorSaveOptions();
    saveOpts.compatibility = Compatibility.ILLUSTRATOR2024;
    doc.saveAs(new File(aiPath), saveOpts);
    
    // === EXPORT PNG (4x scale for high-res) ===
    var pngOpts = new ExportOptionsPNG24();
    pngOpts.horizontalScale = 4.0;
    pngOpts.verticalScale = 4.0;
    pngOpts.antiAliasing = true;
    pngOpts.transparency = false;
    pngOpts.artBoardClipping = true;
    doc.exportFile(new File("C:/Gab/work/Tiktok Managing Agency/logo/TOK_Logo_v3.png"), ExportType.PNG24, pngOpts);
    
    // === EXPORT SVG ===
    var svgOpts = new ExportOptionsSVG();
    svgOpts.compatibility = Compatibility.ILLUSTRATOR2024;
    doc.exportFile(new File("C:/Gab/work/Tiktok Managing Agency/logo/TOK_Logo_v3.svg"), ExportType.SVG, svgOpts);
    
    alert("TOK Logo v3 created!\n\nSaved:\n- TOK_Logo_v3.ai\n- TOK_Logo_v3.png\n- TOK_Logo_v3.svg");
})();
