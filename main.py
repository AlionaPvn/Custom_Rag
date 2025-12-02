

# Die Hauptanwendung:
if __name__ == "__main__":
    # Inhalt + Frage:
    text = """
    Die Sonne ist der Zentralstern des Sonnensystems. Da sie 99,86 % der Gesamtmasse des Systems hat, ist sie sehr nahe dem Baryzentrum des Sonnensystems. In der Reihenfolge ihres Abstands von der Sonne folgen die terrestrischen Planeten Merkur, Venus, Erde und Mars, die den inneren Teil des Planetensystems ausmachen. Den äußeren Teil bilden die Gasplaneten Jupiter, Saturn, Uranus und Neptun. Weitere Begleiter der Sonne sind neben Zwergplaneten Millionen von Asteroiden (auch Planetoiden oder Kleinplaneten genannt) und Kometen, die vorwiegend in drei Kleinkörperzonen des Sonnensystems um die Sonne kreisen: dem Asteroidengürtel zwischen den inneren und den äußeren Planeten, dem Kuipergürtel jenseits der äußeren Planeten und der Oortschen Wolke ganz außen.
    Die Planetenbahnen sind nur wenig gegenüber der Erdbahnebene geneigt, um höchstens 7°, sie liegen also in einer flachen Scheibe. Bei den meisten der bisher (2019) bekannten Kleinplaneten, speziell denen des Kuipergürtels, beträgt die Neigung weniger als 30°. Für die Oortsche Wolke wird dagegen eine Kugelform angenommen.
    Innerhalb der von den einzelnen Sonnenbegleitern beherrschten Raumbereiche - ihrer Hill-Sphären - befinden sich oft kleinere Himmelskörper als umlaufende Begleiter dieser Objekte. Nach dem altbekannten Mond der Erde werden sie analog ebenfalls als Monde, aber auch als Satelliten oder Trabanten bezeichnet. Bis auf den Erdmond und den Plutomond Charon sind sie zumindest bei den Planeten und Zwergplaneten wesentlich kleiner als ihr Hauptkörper. Mondlose Ausnahmen unter den Planeten sind nur Merkur und Venus. Eine definitiv untere Grenzgröße, ab der man wie bei den Bestandteilen der Ringe der Gasplaneten nicht mehr von einem Mond spricht, wurde noch nicht offiziell festgelegt.
    Der Durchmesser der Sonne ist mit etwa 1,39 Millionen Kilometern bei weitem größer als der Durchmesser aller anderen Objekte im System. Die größten dieser Objekte sind die acht Planeten, die vier Jupitermonde Ganymed, Kallisto, Europa und Io (die Galileischen Monde), der Saturnmond Titan und der Erdmond. Zwei Drittel der restlichen Masse von 0,14 % entfallen dabei auf Jupiter. (Siehe auch Liste der größten Objekte im Sonnensystem.)
    Als Folge der Entstehung des Sonnensystems bewegen sich alle Planeten, Zwergplaneten und der Asteroidengürtel auf ihrer Umlaufbahn um die Sonne im gleichen Umlaufsinn, den man rechtläufig nennt. Sie umrunden die Sonne von Norden gesehen gegen den Uhrzeigersinn. Die meisten größeren Monde bewegen sich ebenfalls in diese Richtung um ihren Hauptkörper. Auch die Rotation der meisten größeren Körper des Sonnensystems erfolgt in rechtläufigem Drehsinn. Von den Planeten dreht sich lediglich die Venus entgegengesetzt, und die Rotationsachse von Uranus liegt nahezu in seiner Bahnebene.
    """
    frage = "Wie groß ist der Durchmesser der Sonne?"
    
    # Dokument bzw. Daten in die Wissensdatenbank aufnehmen:
    ingest_document(raw_text=text, source="demo_doc")
    
    # RAG-Antwort erzeugen:
    antowrt = answer_question_with_rag(question=frage)
    print(frage)
    print()
    print(antowrt)
    