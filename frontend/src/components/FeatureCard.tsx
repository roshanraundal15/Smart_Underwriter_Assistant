
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { LucideIcon } from "lucide-react";

interface FeatureCardProps {
  title: string;
  subtitle: string;
  description: string;
  features: string[];
  buttonText: string;
  buttonIcon: LucideIcon;
  icon: LucideIcon;
  gradient: string;
  onAction: () => void;
}

const FeatureCard = ({
  title,
  subtitle,
  description,
  features,
  buttonText,
  buttonIcon: ButtonIcon,
  icon: Icon,
  gradient,
  onAction
}: FeatureCardProps) => {
  return (
    <Card className="group relative overflow-hidden transition-all duration-500 hover:shadow-2xl hover:scale-[1.02] border-0 bg-white/90 backdrop-blur-lg">
      <div className={`absolute inset-0 ${gradient} opacity-10 group-hover:opacity-20 transition-opacity duration-500`} />
      <div className="absolute inset-0 bg-gradient-to-br from-transparent to-black/5" />
      
      <CardHeader className="relative pb-4">
        <div className="flex items-start gap-4 mb-4">
          <div className={`p-3 rounded-2xl ${gradient} bg-opacity-15 shadow-lg`}>
            <Icon className="h-8 w-8 text-white" />
          </div>
          <div className="flex-1">
            <CardTitle className="text-2xl font-bold text-gray-800 mb-2 leading-tight">{title}</CardTitle>
            <p className="text-base font-semibold text-emerald-700">{subtitle}</p>
          </div>
        </div>
        <p className="text-gray-600 leading-relaxed">{description}</p>
      </CardHeader>
      
      <CardContent className="relative space-y-6">
        <div className="grid grid-cols-1 gap-3">
          {features.map((feature, index) => (
            <div key={index} className="flex items-center gap-3 p-2 rounded-lg bg-gray-50/50">
              <div className="w-2 h-2 bg-emerald-500 rounded-full shadow-sm" />
              <span className="text-sm font-medium text-gray-700">{feature}</span>
            </div>
          ))}
        </div>
        
        <Button 
          onClick={onAction}
          className={`w-full ${gradient} hover:shadow-xl transition-all duration-300 text-white font-semibold py-3 rounded-xl`}
        >
          <ButtonIcon className="h-5 w-5 mr-2" />
          {buttonText}
        </Button>
      </CardContent>
    </Card>
  );
};

export default FeatureCard;
